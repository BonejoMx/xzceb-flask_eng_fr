"""
    app for test translator
"""
import unittest
from translator import englis_to_french, french_to_english

# class test english-french
class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englis_to_french('hello'), 'bonjour')

# class test french-english
class TestFrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english('bounjour'), 'hello')

unittest.main()