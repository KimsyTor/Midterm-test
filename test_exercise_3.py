import unittest
from exercise_3 import checkio

class TestCheckio(unittest.TestCase):
    
    # Test if function correctly handles an empty list
    def test_empty_list(self):
        self.assertEqual(checkio([]), 0)

    # Test if function correctly handles a list with a single element
    def test_single_element_list(self):
        self.assertEqual(checkio([5]), 25)

    # Test if function correctly calculates the sum of squares of the elements at even indexes
    def test_even_indexed_elements(self):
        self.assertEqual(checkio([5, 20, 15, 20, 25, 50, 20]), 1300)
        self.assertEqual(checkio([1, 2, 3, 4, 5, 6]), 54)
        self.assertEqual(checkio([0, 0, 0, 0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()
