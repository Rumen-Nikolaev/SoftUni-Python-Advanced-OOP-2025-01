def solution():
    # Generates an infinite sequence of integers starting from 1
    def integers():
        n = 1
        while True:
            yield n
            n += 1

    # Generates the halves of those integers (each integer / 2)
    def halves():
        for i in integers():
            yield i / 2

    # Takes the first n halves of the integers
    def take(n, seq):
        count = 0
        for item in seq:
            if count < n:
                yield item
                count += 1
            else:
                break

    return take, halves, integers
