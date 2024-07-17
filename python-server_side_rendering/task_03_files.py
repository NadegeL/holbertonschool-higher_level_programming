from flask import Flask, render_template, jsonify
import json

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

if __name__ == '__main__':
    app.run(debug=True)

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

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    data = read_data(source)
    
    if product_id:
        filtered_data = [product for product in data if product['id'] == product_id]
        if not filtered_data:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=filtered_data)

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)