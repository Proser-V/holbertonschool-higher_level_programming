#!/usr/bin/python3

from flask import Flask, request
from flask_restful import Api, Resource, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

resource_fields = {
    "id": fields.String,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}

def get_video_or_abort(video_id):
    video = VideoModel.query.get(video_id)
    if not video:
        abort(404, message="Video not found")
    return video

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        return get_video_or_abort(video_id)

    @marshal_with(resource_fields)
    def put(self, video_id):
        if VideoModel.query.get(video_id):
            abort(409, message="Video ID taken...")
        data = request.get_json()
        video = VideoModel(id=video_id, **data)
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        video = get_video_or_abort(video_id)
        data = request.get_json()

        if "name" in data:
            video.name = data["name"]
        if "views" in data:
            video.views = data["views"]
        if "likes" in data:
            video.likes = data["likes"]

        db.session.commit()
        return video

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)