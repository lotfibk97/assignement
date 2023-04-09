from flask import Flask, request, jsonify
import bcrypt

from validations import validate_username_password

app = Flask(__name__)

# In a real application, this would be stored in a database.
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
    # Validate input
        validate_username_password(data)

    except Exception as e:
        return jsonify({'message': 'Validation failed', 'errors': str(e)}), 400

    username = data['username']
    password = data['password']

    # Check if username already exists
    if username in users:
        return jsonify({'message': 'Username already exists'}), 400

    # Encrypt the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users[username] = hashed_password
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        validate_username_password(data)
        
    except Exception as e:
        return jsonify({'message': 'Validation failed', 'errors': str(e)}), 400

    username = data['username']
    password = data['password']

    # Check if username exists
    if username not in users:
        return jsonify({'message': 'Invalid username or password'}), 401

    # Check if password is correct
    if not bcrypt.checkpw(password.encode('utf-8'), users[username]):
        return jsonify({'message': 'Invalid username or password'}), 401

    return jsonify({'message': 'Access granted'}), 200

if __name__ == '__main__':
    app.run()