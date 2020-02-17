import unittest
from spec.metrics.src.counter import Counter


class TestCounter(unittest.TestCase):
    def test_creation(self):
        counter = Counter()
        self.assertEqual(counter.get_count(), 0)

    def test_inc(self):
        counter = Counter()
        counter.inc()
        self.assertEqual(counter.get_count(), 1)
        counter.inc(10)
        self.assertEqual(counter.get_count(), 11)


if __name__ == '__main__':
    unittest.main()
