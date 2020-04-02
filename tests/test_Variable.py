import unittest
from pymint import Variable


class TestVariable(unittest.TestCase):
    def test_int(self):
        x = Variable(5)
        x = x + 2
        self.assertEqual(x, 7)
