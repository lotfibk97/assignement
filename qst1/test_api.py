from api import app
import pytest


# # test valid input for sum endpoint
# @pytest.mark.parametrize('data, expected_sum', [
#     ({'numbers': [1, 2, 3]}, 6),
#     ({'numbers': [-1, 0, 1]}, 0),
#     ({'numbers': [100]}, 100),
# ])
# def test_sum_valid_input(data, expected_sum):
#     with app.test_client() as client:
#         response = client.post('/sum', json=data, content_type='application/json')
#         assert response.status_code == 200
#         assert response.json == {'sum': expected_sum}
#
#
# # test invalid input for sum endpoint
# @pytest.mark.parametrize('data, expected_error', [
#     (None, 'Invalid input. Please provide a JSON object.'),
#     ({'something_else': [1, 2, 3]}, 'Invalid input'),
#     ({'numbers': '1, 2, 3'}, 'Invalid input'),
#     ({'numbers': [1, 2, 'three']}, 'Invalid input'),
#     ({'numbers': []}, 'Invalid input'),
# ])
# def test_sum_invalid_input(data, expected_error):
#     with app.test_client() as client:
#         response = client.post('/sum', json=data, content_type='application/json')
#         print(response.status_code)
#         assert response.status_code == 400
#         assert expected_error in response.json['error']
#
#
# # test valid input for concat endpoint
# @pytest.mark.parametrize('data, expected_concat', [
#     ({'str1': 'Hello', 'str2': 'World!'}, 'HelloWorld!'),
#     ({'str1': 'a', 'str2': 'b'}, 'ab'),
#     ({'str1': '123', 'str2': '456'}, '123456'),
# ])
# def test_concat_valid_input(data, expected_concat):
#     with app.test_client() as client:
#         response = client.post('/concat', json=data, content_type='application/json')
#         assert response.status_code == 200
#         assert response.json == {'concatenated_string': expected_concat}


# test invalid input for concat endpoint
@pytest.mark.parametrize('data, expected_error', [
    ({'str2': 'World!'}, 'Invalid input'),
    ({'str1': 'Hello'}, 'Invalid input'),
    ({'str1': 123, 'str2': 'World!'}, 'Invalid input'),
    ({'str1': 'Hello', 'str2': 456}, 'Invalid input'),
])
def test_concat_invalid_input(data, expected_error):
    with app.test_client() as client:
        response = client.post('/concat', json=data, content_type='application/json')
        assert response.status_code == 400
        assert expected_error in response.json['error']
