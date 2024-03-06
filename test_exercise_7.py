import unittest
from exercise_7 import missing_number

class TestMissingNumber(unittest.TestCase):
    
    def test_missing_number(self):
        
        # Test if function correctly finds the missing number in a sequence
        self.assertEqual(missing_number([1, 4, 2, 5]), 3)

        # Test if function correctly finds the missing number in a sequence
        self.assertEqual(missing_number([2, 6, 8]), 4)

        # Test if function correctly finds the missing number in a sequence
        self.assertEqual(missing_number([10, 20, 30, 40, 50, 60, 80]), 70)

        # Test if function correctly finds the missing number in a sequence
        self.assertEqual(missing_number([1, 3, 4, 5]), 2)

if __name__ == '__main__':
    unittest.main()
