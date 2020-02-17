from spec.metrics.src.metric import Metric


class Counter(Metric):
    def __init__(self, **kwargs):
        self.super(kwargs)
        self._counter = 0

    def inc(self, n=1):
        self._counter += n

    def get_count(self):
        return self._counter
