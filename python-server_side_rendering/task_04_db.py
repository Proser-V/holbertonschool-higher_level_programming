from flask import Flask, render_template, request, abort
import json
import csv
import sqlite3

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

def products_sql():
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM products")
        rows = cursor.fetchall()
        conn.close()

        return [
            {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
            for row in rows
        ]
    except Exception as e:
        raise RuntimeError("Database error: " + str(e))

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

    if source not in ("json", "csv", "sql"):
        return render_template("product_display.html",
                               products=[], message="Wrong source"), 200
    if source == "json":
        data = products_json()
    elif source == "csv":
        data = products_csv()
    else:
        data = products_sql()

    if id:
        try:
            target_id = int(id)
            data = [product for product in data if product["id"] == target_id]
            if not data:
                return render_template("product_display.html", products=[],
                                       message="Product not found"), 200
        except ValueError:
            return render_template("product_display.html", products=[],
                                   message="Product not found"), 200

    return render_template("product_display.html", products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
