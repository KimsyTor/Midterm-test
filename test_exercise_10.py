import unittest
from exercise4 import translate_pig_latin

class TestTranslatePigLatin(unittest.TestCase):
    def test_translate_pig_latin(self):
        
        # Test example 
        self.assertEqual(translate_pig_latin("hello world"), "ellohay orldway")
        
        # Test word starting with a vowel
        self.assertEqual(translate_pig_latin("apple"), "appleway")
        
        # Test word starting with a lowercase letter
        self.assertEqual(translate_pig_latin("quick"), "uickqay")
        
        # Test string with uppercase words
        self.assertEqual(translate_pig_latin("HELLO WORLD"), "ELLOHAY ORLDWAY")

if __name__ == '__main__':
    unittest.main() 
