from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from functions import add_numbers

app = Flask(__name__)
CORS(app)  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<page>')
def render_page(page):
    try:
        return render_template(f'{page}.html')
    except Exception:
        return 'Page Not Found!', 404


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    num1 = data.get('input1')
    num2 = data.get('input2')
    result = 0
    try:
        result = add_numbers(num1, num2)
    except Exception: 
        return jsonify({'error': 'Invalid input'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
