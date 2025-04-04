def vowel_filter(function):
    def wrapper():
        result = function()
        return [char for char in result if char.lower() in 'aeiou']
    return wrapper
