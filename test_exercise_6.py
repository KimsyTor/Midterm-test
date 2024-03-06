import unittest
from exercise_6 import second_index

class TestSecondIndex(unittest.TestCase):

    def test_second_index(self):
        
        # Test if function correctly finds the second occurrence of a character in a string
        self.assertEqual(second_index("sims", "s"), 3)

        # Test if function correctly finds the second occurrence of a character in a string
        self.assertEqual(second_index("hello world", "l"), 3)

        # Test if function correctly finds the second occurrence of a character in a string
        self.assertEqual(second_index("hello world", "o"), 7)

        # Test if function correctly handles a character that does not appear in the string
        self.assertEqual(second_index("hello world", "x"), None)

        # Test if function correctly handles a character that appears only once in the string
        self.assertEqual(second_index("hello world", "h"), None)

        # Test if function correctly handles a character that appears only once in the string
        self.assertEqual(second_index("hello world", "d"), None)

        # Test if function correctly handles a character that appears only once in the string
        self.assertEqual(second_index("hello world", " "), None)

if __name__ == '__main__':
    unittest.main()
