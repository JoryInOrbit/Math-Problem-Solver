from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    num1 = data.get('input1')
    num2 = data.get('input2')

    if num1 is None or num2 is None:
        return jsonify({'error': 'Invalid input'}), 400

    result = num1 + num2

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
