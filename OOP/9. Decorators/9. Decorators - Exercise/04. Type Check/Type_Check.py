def type_check(expected_type):
    def decorator(function):
        def wrapper(*args, **kwargs):
            if all(isinstance(arg, expected_type) for arg in args):
                return function(*args, **kwargs)
            return "Bad Type"
        return wrapper
    return decorator
