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
