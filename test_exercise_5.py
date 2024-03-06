import unittest
from exercise_5 import sum_numbers

class TestSumNumbers(unittest.TestCase):

    def test_sum_numbers(self):

        # Test if function correctly handles a string with no numbers
        self.assertEqual(sum_numbers("hello world"), 0)

        # Test if function correctly sums numbers in a string with mixed words and numbers
        self.assertEqual(sum_numbers("hello 123 world"), 123)

        # Test if function correctly sums numbers in a string with only numbers
        self.assertEqual(sum_numbers("1 2 3 4 5"), 15)

        # Test if function correctly sums numbers in a string with mixed words and numbers
        self.assertEqual(sum_numbers("1 2 three 4 five"), 7)

        # Test if function correctly sums numbers in a string with mixed words and numbers
        self.assertEqual(sum_numbers("1 2 3 4 5 six seven eight nine ten"), 15)

        # Test if function correctly sums numbers in a string with mixed words and numbers
        self.assertEqual(sum_numbers("1 2 3 4 5 six seven eight nine 10"), 25)

        # Test if function correctly sums numbers in a string with mixed words and numbers
        self.assertEqual(sum_numbers("1 2 3 4 5 six seven eight nine ten 11"), 26)

        # Test if function correctly sums numbers in a string with mixed words and numbers
        self.assertEqual(sum_numbers("1 2 3 4 5 six seven eight nine ten 11 12 13"), 51)

if __name__ == '__main__':
    unittest.main()
