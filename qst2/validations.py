def validate_username_password(data):
    if not data:
        raise ValueError('Request body is empty')

    if not isinstance(data, dict):
        raise ValueError('Payload must be a json object')

    if 'username' not in data:
        raise ValueError('Username is required')

    if not isinstance(data['username'], str):
        raise ValueError('Username should be a string')

    if 'password' not in data:
        raise ValueError('Password is required')

    if not isinstance(data['password'], str):
        raise ValueError('Password should be a string')

    validate_username(data['username'])
    validate_password(data['password'])


def validate_username(username):
    if not username:
        raise ValueError('Username is required')

    if len(username) < 3:
        raise ValueError('Username must be at least 3 characters long')



def validate_password(password):
    if not password:
        raise ValueError('Password is required')

    if len(password) < 8:
        raise ValueError('Password must be at least 8 characters long')

