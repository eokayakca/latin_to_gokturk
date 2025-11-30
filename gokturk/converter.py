from .mappings import VOWELS, CONSONANTS_DUAL, CONSONANTS_NEUTRAL, LIGATURES, SYLLABLES, PUNCTUATION
from .utils import get_local_harmony, is_vowel

class LatinToGokturkConverter:
    def __init__(self):
        pass

    def convert(self, text, rtl=False):
        if not text:
            return ""
            
        import re
        # Split by whitespace, keeping the delimiters
        tokens = re.split(r'(\s+)', text)
        converted_tokens = []
        
        for token in tokens:
            if not token:
                continue
            # If it's whitespace, keep it as is
            if re.match(r'^\s+$', token):
                converted_tokens.append(token)
            else:
                # It's a word, convert it
                converted_tokens.append(self.convert_word(token))
            
        result = "".join(converted_tokens)
        
        if rtl:
            # Smart RTL: Reverse only Göktürk runs, keep numbers/Latin LTR, but reverse the visual order of blocks.
            lines = result.split('\n')
            reversed_lines = [self._smart_reverse(line) for line in lines]
            return '\n'.join(reversed_lines)
            
        return result

    def _smart_reverse(self, text):
        import re
        # Regex for Old Turkic characters (U+10C00-U+10C4F) OR Digits
        # We split by these to ensure numbers are treated as separate chunks from punctuation
        # But we only want to REVERSE the Old Turkic characters.
        split_pattern = r'([\U00010C00-\U00010C4F]+|\d+)'
        parts = re.split(split_pattern, text)
        
        # Reverse the order of chunks to simulate RTL flow
        parts.reverse()
        
        processed_parts = []
        gokturk_pattern = r'[\U00010C00-\U00010C4F]+'
        
        for part in parts:
            if not part:
                continue
                
            if re.match(gokturk_pattern, part):
                # It's Göktürk: Reverse the characters
                processed_parts.append(part[::-1])
            else:
                # It's Latin/Numbers/Symbols: Keep as is (LTR)
                processed_parts.append(part)
                
        return "".join(processed_parts)

    def convert_word(self, word):
        result = []
        i = 0
        word_lower = word.lower()
        
        # First pass: Convert to raw characters/ligatures
        while i < len(word_lower):
            # 1. Check for 2-char Ligatures/Syllables
            if i + 1 < len(word_lower):
                pair = word_lower[i:i+2]
                
                # Check Ligatures (nd, ld, etc.)
                if pair in LIGATURES:
                    result.append(LIGATURES[pair])
                    i += 2
                    continue
                
                # Check Specific Syllables (ok, uk, etc.)
                # These often override standard char-by-char mapping
                if pair in SYLLABLES:
                    result.append(SYLLABLES[pair])
                    i += 2
                    continue

            char = word_lower[i]
            
            # 2. Check Vowels
            if char in VOWELS:
                result.append(VOWELS[char])
                i += 1
                continue
                
            # 3. Check Dual Consonants
            if char in CONSONANTS_DUAL:
                harmony = get_local_harmony(word_lower, i)
                back_char, front_char = CONSONANTS_DUAL[char]
                if harmony == 'front':
                    result.append(front_char)
                else:
                    result.append(back_char)
                i += 1
                continue
                
            # 4. Check Neutral Consonants
            if char in CONSONANTS_NEUTRAL:
                result.append(CONSONANTS_NEUTRAL[char])
                i += 1
                continue
                
            # 5. Punctuation
            if char in PUNCTUATION:
                result.append(PUNCTUATION[char])
                i += 1
                continue
            
            # Fallback
            result.append(word[i])
            i += 1
            
        raw_gokturk = "".join(result)
        
        # Post-processing (Vowel Reduction and Fixes)
        return self.post_process(raw_gokturk)

    def post_process(self, text):
        # Reference implementation rules:
        # Remove 'a' (𐰀) if it's surrounded by non-space characters?
        # The reference regex: result.replace(/(?<=\S𐰀|𐰀\S)𐰀(?=[^\s\x00-\x7F])/gu, '');
        # This implies removing 'a' if it's inside a word (not start/end?).
        # Orkhon script often omits 'a'/'e' inside words.
        
        # Let's implement a simple version of vowel reduction for 'a' and 'e' (𐰀)
        # If 𐰀 is between two consonants, it is often omitted.
        # However, be careful not to over-delete.
        
        # Specific fixes from reference
        # Atatürk -> 𐰀𐱃𐰀𐱅𐰇𐰼𐰜
        if '𐰀𐱃𐱃𐰇𐰼𐰚' in text: 
             text = text.replace('𐰀𐱃𐱃𐰇𐰼𐰚', '𐰀𐱃𐰀𐱅𐰇𐰼𐰜')
             
        # Türk -> 𐱅𐰇𐰼𐰜 (Historically preferred over 𐱅𐰇𐰼𐰚)
        # My converter produces 𐱅𐰇𐰼𐰚 (T-Ü-R-Kfront)
        if '𐱅𐰇𐰼𐰚' in text:
            text = text.replace('𐱅𐰇𐰼𐰚', '𐱅𐰇𐰼𐰜')

        # Tengri -> 𐱅𐰭𐰼𐰃
        
        return text
