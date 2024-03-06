import unittest
from exercise_2 import checkio

class TestCheckio(unittest.TestCase):
    def test_non_unique_elements(self):
        
        # Test if function correctly identifies 
        # and returns non-unique elements in a list with some duplicates
        self.assertEqual(checkio([1, 2, 3, 1, 3]), [1, 3, 1, 3])

        # Test if function correctly identifies 
        # and returns non-unique elements in a list with all elements duplicated
        self.assertEqual(checkio([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 
                                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

        # Test if function correctly identifies 
        # and returns non-unique elements in a list with all elements the same
        self.assertEqual(checkio([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])

        # Test if function correctly handles a list with no duplicates
        self.assertEqual(checkio([1, 2, 3, 4, 5]), [])

        # Test if function correctly handles a list with a single element
        self.assertEqual(checkio([1]), [])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
