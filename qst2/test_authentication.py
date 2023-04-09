import json
import pytest
import bcrypt
from authentication import app, users
from validations import validate_username_password,validate_password,validate_username

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_register(client):
    # test successful registration
    response = client.post('/register', json={'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 201
    assert response.json['message'] == 'User registered successfully'

    # test registration with an already existing username
    response = client.post('/register', json={'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 400
    assert response.json['message'] == 'Username already exists'

def test_login(client):
    # test successful login
    hashed_password = bcrypt.hashpw('testpassword'.encode('utf-8'), bcrypt.gensalt())
    users['testuser'] = hashed_password
    response = client.post('/login', json={'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 200
    assert response.json['message'] == 'Access granted'

    # test login with incorrect password
    response = client.post('/login', json={'username': 'testuser', 'password': 'wrongpassword'})
    assert response.status_code == 401
    assert response.json['message'] == 'Invalid username or password'

    # test login with non-existent username
    response = client.post('/login', json={'username': 'nonexistentuser', 'password': 'testpassword'})
    assert response.status_code == 401
    assert response.json['message'] == 'Invalid username or password'

def test_validate_username_password():
    # test valid input
    data = {'username': 'testuser', 'password': 'testpassword'}
    assert validate_username_password(data) == None

    # test empty input
    with pytest.raises(ValueError, match=r'Request body is empty'):
        data = {}
        validate_username_password(data)

    # test non-dict input
    with pytest.raises(ValueError, match=r'Payload must be a json object'):
        data = 'not a dictionary'
        validate_username_password(data)

    # test missing username
    with pytest.raises(ValueError, match=r'Username is required'):
        data = {'password': 'testpassword'}
        validate_username_password(data)

    # test missing password
    with pytest.raises(ValueError, match=r'Password is required'):
        data = {'username': 'testuser'}
        validate_username_password(data)

    # test non-string username
    with pytest.raises(ValueError, match=r'Username should be a string'):
        data = {'username': 1234, 'password': 'testpassword'}
        validate_username_password(data)

    # test non-string password
    with pytest.raises(ValueError, match=r'Password should be a string'):
        data = {'username': 'testuser', 'password': 1234}
        validate_username_password(data)

def test_validate_username():
    # test valid input
    username = 'testuser'
    assert validate_username(username) == None

    # test missing username
    with pytest.raises(ValueError, match=r'Username is required'):
        username = ''
        validate_username(username)

    # test username with less than 3 characters
    with pytest.raises(ValueError, match=r'Username must be at least 3 characters long'):
        username = 'a'
        validate_username(username)

def test_validate_password():
    # test valid input
    password = 'testpassword'
    assert validate_password(password) == None

    # test