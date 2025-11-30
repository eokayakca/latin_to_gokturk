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
        # Türk -> T-Ü-R-K (front)
        # Updated logic uses historical fix: 𐱅𐰇𐰼𐰜
        self.assertEqual(self.converter.convert("Türk"), "𐱅𐰇𐰼𐰜")
        # Gök -> G-ÖK -> 𐰏𐰜 (syllable optimization)
        self.assertEqual(self.converter.convert("Gök"), "𐰏𐰜")

    def test_basic_back_vowels(self):
        # Dağ -> D-A-Ğ (back)
        self.assertEqual(self.converter.convert("Dağ"), "𐰑𐰀𐰍")
        # Ok -> O-K (back) -> 𐰸 (special mapping)
        self.assertEqual(self.converter.convert("Ok"), "𐰸")

    def test_clusters(self):
        # Tengri -> T-E-NG-R-I
        self.assertEqual(self.converter.convert("Tengri"), "𐱅𐰜𐰭𐰼𐰃")

    def test_sentences(self):
        # "Türk Gök" -> "𐱅𐰇𐰼𐰜 𐰏𐰜" (Space preserved, no colon)
        self.assertEqual(self.converter.convert("Türk Gök"), "𐱅𐰇𐰼𐰜 𐰏𐰜")

    def test_case_insensitivity(self):
        self.assertEqual(self.converter.convert("türk"), "𐱅𐰇𐰼𐰜")

if __name__ == '__main__':
    unittest.main()
