import unittest
from machinetranslation import translator

class EnglishToFrench(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")
    
    # def test2(self):
    #     self.???(englishToFrench(None))


class FrenchToEnglish(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")
    
    # def test2(self):
    #     self.???(frenchToEnglish(None))

unittest.main()