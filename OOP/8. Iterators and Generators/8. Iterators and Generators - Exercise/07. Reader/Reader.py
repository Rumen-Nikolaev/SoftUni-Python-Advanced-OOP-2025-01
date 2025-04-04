def read_next(*args):
    iterators = [iter(arg) for arg in args]
    while iterators:
        for it in iterators:
            try:
                yield next(it)
            except StopIteration:
                iterators.remove(it)
