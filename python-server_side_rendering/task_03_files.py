from flask import Flask, render_template, request, abort
import json
import csv


app = Flask(__name__)

def products_json():
    with open("products.json", "r") as file:
        return json.load(file)

def products_csv():
    products_list = []
    with open("products.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products_list.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products_list

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open("items.json", "r") as file:
        data = json.load(file)
        items_list = data.get("items", [])
    return render_template('items.html', items=items_list)


@app.route('/products')
def display_products():
    source = request.args.get("source")
    id = request.args.get("id")

    if source not in ("json", "csv"):
        return render_template("product_display.html",
                               products=[], message="Wrong source"), 200
    if source == "json":
        data = products_json()
    else:
        data = products_csv()

    if id:
        try:
            target_id = int(id)
            data = [product for product in data if product["id"] == target_id]
        except ValueError:
            return abort(400, "Product not found")

    return render_template("product_display.html", products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
