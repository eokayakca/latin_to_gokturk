import unittest
import sys
import os

# Add the package to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gokturk.converter import LatinToGokturkConverter

class TestDetailedConverter(unittest.TestCase):
    def setUp(self):
        self.converter = LatinToGokturkConverter()

    def test_mixed_harmony_words(self):
        # "Kitap": 'i' (front) -> K should be front (𐰚), 'a' (back) -> t should be back (𐱃)?
        # Or does the whole word take the dominant harmony?
        # Current implementation: dominant harmony.
        # Kitap: 1 front, 1 back. Dominant? 
        # If front: 𐰚𐰃𐱅𐰀𐰯 (Ki-t-a-p) -> K(front) i t(front) a p
        # If back: 𐰴𐰃𐱃𐰀𐰯 (K-i-t-a-p) -> K(back) i t(back) a p
        # Correct Göktürk for Kitap (loanword) is tricky. Usually written phonetically.
        # Let's just see what it produces and if it crashes.
        res = self.converter.convert("Kitap")
        print(f"Kitap -> {res}")
        self.assertTrue(len(res) > 0)

    def test_foreign_characters(self):
        # "Japonya": J?
        res = self.converter.convert("Japonya")
        print(f"Japonya -> {res}")
        # "Vazo": V -> B?
        res = self.converter.convert("Vazo")
        print(f"Vazo -> {res}")
        # "Fare": F -> P?
        res = self.converter.convert("Fare")
        print(f"Fare -> {res}")
        # "Cuma": C?
        res = self.converter.convert("Cuma")
        print(f"Cuma -> {res}")

    def test_clusters_in_context(self):
        # "Hangi" -> ng -> 𐰭
        res = self.converter.convert("Hangi")
        print(f"Hangi -> {res}")
        self.assertIn('𐰭', res)

    def test_punctuation_handling(self):
        res = self.converter.convert("Merhaba, Dünya.")
        # Should be "Merhaba : Dünya" (dots removed, comma -> :)
        print(f"Merhaba, Dünya. -> {res}")
        self.assertNotIn('.', res)
        self.assertNotIn(',', res)
        self.assertIn(':', res)

if __name__ == '__main__':
    unittest.main()
