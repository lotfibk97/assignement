
# Basic API

This is a basic API built with Python and Flask. It has two endpoints:

- `/sum`: Accepts a list of numbers and returns their sum.
- `/concat`: Accepts two strings and concatenates them.

## Requirements
- Python 3.x
- Flask

## Installation
1. Clone the repository: `git clone https://github.com/lotfibk97/assignement.git`
2. Navigate to the project directory: `cd qst1`
3. Install the dependencies: `pip install -r requirements.txt`

## Usage
1. Start the server: `flask --app api run`
2. Open your web browser or API testing tool and make a POST request to `http://localhost:5000/sum` or `http://localhost:5000/concat` with the appropriate JSON data.

### /sum
- Method: POST
- URL: `http://localhost:5000/sum`
- Request body: JSON object with a single key, `numbers`, which is a list of numbers.

Example:

```json
{
    "numbers": [1, 2, 3]
}
```
Response:

```json
{
    "sum": 6
}
```
### /concat
 - Method: POST
 - URL: http://localhost:5000/concat
 - Request body: JSON object with two keys, str1 and str2, which are strings.
Example:

```json
{
    "str1": "Hello",
    "str2": "World!"
}
```
Response:

```json
{
    "concatenated_string": "HelloWorld!"
}
```
## Testing
 - To run the tests, use the command `pytest` in the project directory.

