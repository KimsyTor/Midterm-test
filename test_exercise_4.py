import unittest
from exercise_4 import backward_string_by_word

class TestBackwardStringByWord(unittest.TestCase):

    # Test if function correctly reverses a single word
    def test_single_word(self):
        self.assertEqual(backward_string_by_word("hello"), "olleh")

    # Test if function correctly reverses each word in a string with multiple words
    def test_multiple_words(self):
        self.assertEqual(backward_string_by_word("hello world"), "olleh dlrow")

    # Test if function correctly handles an empty string
    def test_empty_string(self):
        self.assertEqual(backward_string_by_word(""), "")

    # Test if function correctly reverses each word in a string with multiple words and extra spaces
    def test_string_with_spaces(self):
        self.assertEqual(backward_string_by_word("   hello   world   "), "   olleh   dlrow   ")

if __name__ == '__main__':
    unittest.main()
