class Counter:
    def __init__(self):
        self._counter = 0

    def inc(self, n=0):
        self._counter += n

    def get_count(self):
        return self._counter
