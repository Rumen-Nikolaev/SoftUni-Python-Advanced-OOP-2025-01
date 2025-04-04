class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        self.current = self.count
        return self

    def __next__(self):
        if self.current >= 0:
            current_value = self.current
            self.current -= 1
            return current_value
        raise StopIteration
