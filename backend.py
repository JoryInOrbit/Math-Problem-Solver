from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from functions import solve_arithmetic_expression

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
    expression = data.get('expression')
    result = 0
    try:
        result = solve_arithmetic_expression(expression)
    except Exception: 
        return jsonify({'error': 'Invalid input'}), 400
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
