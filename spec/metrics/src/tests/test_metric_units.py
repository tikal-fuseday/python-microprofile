import unittest
from spec.metrics.src.metric_units import MetricUnits


class TestMetricUnits(unittest.TestCase):
    def test_metric_from(self):
        self.assertEqual(MetricUnits.GIBIBITS, MetricUnits.unit_from('gibibits'))

    def test_metric_from_not_exists(self):
        self.assertEqual(MetricUnits.NONE, MetricUnits.unit_from('bla'))


if __name__ == '__main__':
    unittest.main()
