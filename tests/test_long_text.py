import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gokturk.converter import LatinToGokturkConverter

class TestLongText(unittest.TestCase):
    def setUp(self):
        self.converter = LatinToGokturkConverter()

    def test_genclige_hitabe_start(self):
        text = "Ey Türk Gençliği! Birinci vazifen, Türk istiklâlini, Türk Cumhuriyetini, ilelebet, muhafaza ve müdafaa etmektir."
        print(f"\nOriginal: {text}")
        res = self.converter.convert(text)
        print(f"Göktürk: {res}")
        
        # Basic checks
        self.assertIn("𐱅𐰇𐰼𐰜", res) # Türk
        self.assertTrue(len(res) > len(text)) # Should be roughly similar or longer due to unicode bytes, but logically just check it's not empty

    def test_bilge_kagan(self):
        # A snippet from Bilge Kagan inscription (modern Turkish translation)
        text = "Tanrı gibi gökte olmuş Türk Bilge Kağanı, bu zamanda oturdum. Sözümü tam işitin."
        print(f"\nOriginal: {text}")
        res = self.converter.convert(text)
        print(f"Göktürk: {res}")

if __name__ == '__main__':
    unittest.main()
