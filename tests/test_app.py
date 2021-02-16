import unittest

class TestClass(unittest.TestCase):

    def setUp(self):
        pass

    def test_useless_assert(self):
        self.assertEqual('1', '1')
