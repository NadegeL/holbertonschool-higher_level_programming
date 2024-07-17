from flask import Flask, render_template, request
import json
import os
import csv

app = Flask(__name__)

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
    items_file_path = os.path.join(os.path.dirname(__file__), 'items.json')
    with open(items_file_path, 'r', encoding='UTF-8') as f:
        data = json.load(f)

    items = data.get('items', [])
    return render_template('items.html', items=items)

@app.route('/products')
def product_display():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error_message = None

    if source == 'json':
        product_json_file_path = os.path.join(os.path.dirname(__file__), 'products.json')
        with open(product_json_file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                products = data
            else:
                products = data.get('products', dict)

    elif source == 'csv':
        product_csv_file_path = os.path.join(os.path.dirname(__file__), 'products.csv')
        with open(product_csv_file_path, 'r', encoding='UTF-8') as f:
            reader = csv.DictReader(f)
            products = list(reader)

    else:
        error_message = "Wrong source"

    if product_id and not error_message:
        products = [product for product in products if str(product.get('id')) == str(product_id)]

    return render_template('products.html', products=products, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)