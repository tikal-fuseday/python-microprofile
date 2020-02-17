import unittest
from spec.metrics.src.counter import Counter
from spec.metrics.src.metric_units import MetricUnits
from spec.metrics.src.metric_types import MetricTypes


class TestCounter(unittest.TestCase):
    def test_creation(self):
        counter = Counter('test_metric', MetricUnits.NONE, MetricTypes.COUNTER)
        self.assertEqual(counter.get_count(), 0)

    def test_inc(self):
        counter = Counter('test_metric', MetricUnits.NONE, MetricTypes.COUNTER)
        counter.inc()
        self.assertEqual(counter.get_count(), 1)
        counter.inc(10)
        self.assertEqual(counter.get_count(), 11)


if __name__ == '__main__':
    unittest.main()
