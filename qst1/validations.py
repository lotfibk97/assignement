def validate_sum_input(data):
    if data is None:
        raise ValueError('Invalid input. Please provide a JSON object.')
    
    if 'numbers' not in data:
        raise ValueError('Invalid input. Please provide a JSON object with a "numbers" key.')
    
    numbers = data['numbers']
    
    if len(numbers) == 0:
        raise ValueError('Invalid input')
    
    if not isinstance(numbers, list):
        raise ValueError('Invalid input. "numbers" key must contain a list of numbers.')
    
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError('Invalid input. All elements in "numbers" list must be numbers.')
    
    return None


def validate_concat_input(data):
    if not data:
        raise ValueError('Invalid input. Please provide a JSON object.')
    
    if 'str1' not in data or 'str2' not in data:
        raise ValueError('Invalid input. Please provide a JSON object with "str1" and "str2" keys.')
    
    str1 = data['str1']
    str2 = data['str2']
    
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError('Invalid input. "str1" and "str2" must be strings.')
    
    return None
