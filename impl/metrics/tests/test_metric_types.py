import unittest
from impl.metrics.metric_types import MetricTypes


class TestMetricTypes(unittest.TestCase):
    def test_metric_from(self):
        self.assertEqual(MetricTypes.CONCURRENT_GAUGE, MetricTypes.metric_from('concurrent gauge'))

    def test_metric_from_not_exists(self):
        self.assertEqual(MetricTypes.INVALID, MetricTypes.metric_from('bla'))


if __name__ == '__main__':
    unittest.main()
