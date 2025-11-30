import unittest
import sys
import os

# Add the package to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gokturk.converter import LatinToGokturkConverter

class TestLatinToGokturkConverter(unittest.TestCase):
    def setUp(self):
        self.converter = LatinToGokturkConverter()

    def test_basic_front_vowels(self):
        # Türk -> 𐱅𐰇𐰼𐰚
        self.assertEqual(self.converter.convert("Türk"), "𐱅𐰇𐰼𐰚")
        # Gök -> 𐰏𐰇𐰚
        self.assertEqual(self.converter.convert("Gök"), "𐰏𐰇𐰚")

    def test_basic_back_vowels(self):
        # Dağ -> 𐰑𐰀𐰍
        self.assertEqual(self.converter.convert("Dağ"), "𐰑𐰀𐰍")
        # Ok -> 𐰆𐰴
        self.assertEqual(self.converter.convert("Ok"), "𐰆𐰴")

    def test_clusters(self):
        # Tengri -> 𐱅𐰜𐰭𐰼𐰃
        # Note: 'ng' is 𐰭
        self.assertEqual(self.converter.convert("Tengri"), "𐱅𐰜𐰭𐰼𐰃")

    def test_sentences(self):
        # Türk Gök -> 𐱅𐰇𐰼𐰚 : 𐰏𐰇𐰚
        self.assertEqual(self.converter.convert("Türk Gök"), "𐱅𐰇𐰼𐰚 : 𐰏𐰇𐰚")

    def test_case_insensitivity(self):
        self.assertEqual(self.converter.convert("türk"), "𐱅𐰇𐰼𐰚")

if __name__ == '__main__':
    unittest.main()
