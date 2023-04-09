from flask import Flask, jsonify, request
from validations import validate_sum_input, validate_concat_input
from business_logic import sum_numbers, concat_strings
import logging

import sys




app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/sum', methods=['POST'])
def sum_endpoint():
    try:
        data = request.json
        validate_sum_input(data)
        result = sum_numbers(data['numbers'])
        return jsonify({'sum': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/concat', methods=['POST'])
def concat_endpoint():
    try:
        data = request.json
        validate_concat_input(data)
        result = concat_strings(data['str1'], data['str2'])
        return jsonify({'concatenated_string': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)