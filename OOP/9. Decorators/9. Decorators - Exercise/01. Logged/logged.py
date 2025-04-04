def logged(function):
    def wrapper(*args, **kwargs):
        # Call the original function
        result = function(*args, **kwargs)
        # Print the function name, arguments, and the result
        print(f'you called {function.__name__}({", ".join(map(str, args))})')
        print(f'it returned {result}')
        return result
    return wrapper
