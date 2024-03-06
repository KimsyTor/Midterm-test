import unittest
from exercise_1 import duplicate_zeros

class TestDuplicateZeros(unittest.TestCase):
    def test_duplicate_zeros(self):

        # Test if function correctly duplicates zeros in a list with mixed numbers
        self.assertEqual(duplicate_zeros([1, 0, 2, 0]), [1, 0, 0, 2, 0, 0])

        # Test if function correctly duplicates zeros in a list with only zeros
        self.assertEqual(duplicate_zeros([0, 0, 0, 0]), [0, 0, 0, 0, 0, 0, 0, 0])

        # Test if function correctly handles a list with no zeros
        self.assertEqual(duplicate_zeros([1, 2, 3, 4]), [1, 2, 3, 4])

        # Test if function correctly duplicates zeros in a list with zeros interspersed with other numbers
        self.assertEqual(duplicate_zeros([0, 1, 0, 2, 0, 3, 0]), [0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0])

        # Test if function correctly handles an empty list
        self.assertEqual(duplicate_zeros([]), [])

if __name__ == '__main__':
    unittest.main()
