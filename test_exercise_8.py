import unittest
from exercise7 import find_missing_number

class TestFindMissingNumber(unittest.TestCase):
    
    def test_find_missing_number(self):
        
        # list with multiple gaps. Expected output is [5, 9, 12]
        self.assertEqual(find_missing_number([2, 3, 4, 6, 7, 8, 10, 11, 13, 14, 15]), [5, 9, 12])
        
        # list with a single gap. Expected output is [6, 8]
        self.assertEqual(find_missing_number([5, 7, 9]), [6, 8])
        
        # list with no gaps. Expected output is an empty list
        self.assertEqual(find_missing_number([1, 2, 3, 4, 5]), [])
        
        # empty list. Expected output is an empty list
        self.assertEqual(find_missing_number([]), [])

if __name__ == '__main__':
    unittest.main()
