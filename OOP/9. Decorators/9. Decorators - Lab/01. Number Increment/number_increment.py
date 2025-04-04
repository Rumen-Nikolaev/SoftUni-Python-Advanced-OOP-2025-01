def number_increment(numbers):
    def increase():
        for num in numbers:
            yield num + 1
    return list(increase())
