import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gokturk.converter import LatinToGokturkConverter

class TestLigatures(unittest.TestCase):
    def setUp(self):
        self.converter = LatinToGokturkConverter()

    def test_ligatures(self):
        # and -> 𐰀𐰦 (a + nd)
        res = self.converter.convert("and")
        print(f"and -> {res}")
        self.assertIn('𐰦', res)
        
        # alt -> 𐰀𐰡 (a + lt)
        res = self.converter.convert("alt")
        print(f"alt -> {res}")
        self.assertIn('𐰡', res)
        
        # inç -> 𐰃𐰨 (i + nç)
        res = self.converter.convert("inç")
        print(f"inç -> {res}")
        self.assertIn('𐰨', res)

    def test_specific_syllables(self):
        # ok -> 𐰸 (not o+k)
        res = self.converter.convert("ok")
        print(f"ok -> {res}")
        self.assertEqual(res, "𐰸")
        
        # çok -> 𐰲𐰸
        res = self.converter.convert("çok")
        print(f"çok -> {res}")
        self.assertEqual(res, "𐰲𐰸")

    def test_full_sentences_with_ligatures(self):
        # "Türk milleti" -> Türk: 𐱅𐰇𐰼𐰜 (k is front), milleti: ...
        # milleti -> m i l l e t i -> 𐰢 𐰃 𐰠 𐰠 𐰜 𐱅 𐰃
        # Let's see what happens
        res = self.converter.convert("Türk milleti")
        print(f"Türk milleti -> {res}")

if __name__ == '__main__':
    unittest.main()
