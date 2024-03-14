import unittest
from exercise5 import count_rhyme

class TestCountRhyme(unittest.TestCase):
    def test_count_rhyme(self):

        # empty list
        self.assertEqual(count_rhyme([], 'bat'), 0)

        # list with one word that doesn't rhyme
        self.assertEqual(count_rhyme(['pig'], 'bat'), 0)

        # list with two words that don't rhyme
        self.assertEqual(count_rhyme(['cat', 'dog'], 'bat'), 1)

        # list with two words that rhyme
        self.assertEqual(count_rhyme(['cat', 'hat'], 'bat'), 2)

        # list with multiple words and some of them rhyme
        self.assertEqual(count_rhyme(['cat', 'hat', 'dog', 'mat'], 'bat'), 3)

if __name__ == '__main__':
    unittest.main()
