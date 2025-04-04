class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.number > 0:
            current_value = self.sequence[self.index]
            self.index = (self.index + 1) % len(self.sequence)
            self.number -= 1
            return current_value
        raise StopIteration
