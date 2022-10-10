import math
import unittest
from square import squareroot

class TestSquareRoot(unittest.TestCase):

    def test_negativeGivenNumber(self):
        with self.assertRaises(Exception):
            squareroot(-12)

    def test_positiveGivenNumber(self):
        self.assertEqual(squareroot(1), math.sqrt(1))
        self.assertEqual(squareroot(4), math.sqrt(4))
        self.assertEqual(squareroot(15), math.sqrt(15))
        self.assertEqual(squareroot(1689), math.sqrt(1689))
        self.assertEqual(squareroot(122546), math.sqrt(122546))
        
if __name__ == '__main__':
    unittest.main()