from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)

    items_list = data.get('items', [])

    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    source = request.args.get('source', default=None, type=str)
    id = request.args.get('id', default=None, type=str)

    if source not in ["json", "csv"]:
        return render_template('product_display.html', error_message='Invalid source')

    if source == "json":
        with open('products.json') as file:
            data = json.load(file)
    else:  # source == "csv"
        with open('products.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

    if id:
        data = [product for product in data if product['id'] == id]

    if not data:
        return render_template('product_display.html', error_message="No products found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
