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
        # Göktürk text is often shorter in characters due to ligatures/omitted vowels, 
        # but unicode bytes might be longer. Let's just check it's not empty and reasonable.
        self.assertTrue(len(res) > 0)

    def test_bilge_kagan(self):
        # A snippet from Bilge Kagan inscription (modern Turkish translation)
        text = "Tanrı gibi gökte olmuş Türk Bilge Kağanı, bu zamanda oturdum. Sözümü tam işitin."
        print(f"\nOriginal: {text}")
        res = self.converter.convert(text)
        print(f"Göktürk: {res}")

if __name__ == '__main__':
    unittest.main()
