import unittest
from demo.metrics.tag import Tag


class TestTag(unittest.TestCase):
    def test_create_instance(self):
        tag = Tag('name', 'value')
        self.assertEqual(tag.get_tag_name(), 'name')
        self.assertEqual(tag.get_tag_value(), 'value')

    def test_create_raises_exception(self):
        bad_name = lambda: Tag('_%&$#@', 'value')
        self.assertRaises(Exception, bad_name)

    def test_equals(self):
        tag1 = Tag('name', 'value')
        tag2 = Tag('name', 'value')
        self.assertEqual(tag1, tag2)


if __name__ == '__main__':
    unittest.main()
