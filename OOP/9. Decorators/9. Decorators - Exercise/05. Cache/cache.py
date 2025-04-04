def cache(func):
    def wrapper(n):
        if not hasattr(func, 'log'):
            func.log = {} 
        if n not in func.log: 
            func.log[n] = func(n)  
        return func.log[n] 
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
