def calculate(operation, a, b, make_int=False, message='The result is'):
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b == 0:
            return None
        result = a / b
    
    if make_int: 
        result = int(result)
    return f'{message} {result}'