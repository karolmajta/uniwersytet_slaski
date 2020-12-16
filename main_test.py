import unittest

from main import find_user_by_id

class ArithmeticOperationsTestCase(unittest.TestCase):
    
    def test_addition(self):
        assert 2 + 2 == 4, "Addition should just work"
    
    def test_subtraction(self):
        self.assertEqual(2 - 2, 0)