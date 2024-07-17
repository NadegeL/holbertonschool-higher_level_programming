from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def load_items():
    with open('items.json') as f:
        data = json.load(f)
    return data['items']


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
    with open('items.json') as f:
        item = json.load(f).get("items", [])
    return render_template('items.html', items=item), 200


def read_data(source):
    if source == 'json':
        return read_json('products.json')
    elif source == 'csv':
        return read_csv('products.csv')


def read_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def read_csv(filepath):
    with open(filepath, newline='') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

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
