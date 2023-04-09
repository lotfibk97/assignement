# Flask Authentication API

This is a simple Flask API for user authentication using bcrypt to hash passwords.

## Installation

1. Clone the repository
2. Install the requirements using pip: `pip install -r requirements.txt`
3. Run the app: `flask --app api run`

## API Endpoints

### Register

**Endpoint:** `/register`<br>
**Method:** POST<br>
**Input:** JSON object with `username` and `password` fields<br>
**Output:** JSON object with a message field

Registers a new user with the given username and password.

### Login

**Endpoint:** `/login`<br>
**Method:** POST<br>
**Input:** JSON object with `username` and `password` fields<br>
**Output:** JSON object with a message field

Authenticates a user with the given username and password.

## Validation

The input to both the `/register` and `/login` endpoints is validated using the following rules:

- The input must be a JSON object.
- The JSON object must have `username` and `password` fields.
- The `username` field must be a string of at least 3 characters.
- The `password` field must be a string of at least 8 characters.

## Testing

Testing is done using pytest. To run the tests, use the following command:

```sh
pytest
