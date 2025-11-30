# Mappings for Latin to Göktürk conversion

# Vowels
VOWELS = {
    'a': '𐰀', 'e': '𐰀',
    'ı': '𐰃', 'i': '𐰃',
    'o': '𐰆', 'u': '𐰆',
    'ö': '𐰇', 'ü': '𐰇',
    'â': '𐰀', 'î': '𐰃', 'û': '𐰆' # Circumflex vowels mapped to standard vowels
}

# Syllable Maps (Back Vowels)
# These represent specific combinations often used in the script.
# Note: The JS reference maps 'ab' -> '𐰀𐰉' which is just A+B. 
# But some are specific like 'ik' -> '𐰶' (which is actually a specific character Iduk/Ik).
# Let's define the special ones that are NOT just concatenation.
# If it is just concatenation, our logic can handle it.
# However, the JS code uses these maps to drive harmony state.
# We will stick to our dynamic harmony logic but add the special ligatures.

# Special Ligatures / Clusters
# These are characters that represent two sounds or specific combinations.
LIGATURES = {
    'nd': '𐰦',
    'nt': '𐰦',
    'ld': '𐰡',
    'lt': '𐰡',
    'nç': '𐰨',
    'ny': '𐰪',
    'ng': '𐰭',
    'nk': '𐰭', # Sometimes nk is ng
}

# Specific Syllable Characters (Irregular or specific glyphs)
# ik/ık -> 𐰶 (sometimes used for 'q' sound or 'ik')
# ok/uk -> 𐰸
# ük/ök -> 𐰜 (same as e/a sometimes? No, 𐰜 is usually 'ök' or 'kü')
# Let's map these carefully.
# In standard Orkhon:
# 𐰶 is 'iq' / 'q' (back k)
# 𐰸 is 'oq' / 'uq' (back k rounded)
# 𐰜 is 'ök' / 'ük' (front k rounded) - Wait, 𐰜 is usually 'e' or 'ae'. 
# Actually 𐰜 is often used for 'ök'.
# Let's follow the reference for these specific overrides.
SYLLABLES = {
    'ık': '𐰶',
    'ok': '𐰸',
    'uk': '𐰸',
    'ök': '𐰜',
    'ük': '𐰜',
}

# Consonants that have back/front variations
CONSONANTS_DUAL = {
    'b': ('𐰉', '𐰋'),
    'd': ('𐰑', '𐰓'),
    'g': ('𐰍', '𐰏'), 
    'ğ': ('𐰍', '𐰏'),
    'k': ('𐰴', '𐰚'),
    'l': ('𐰞', '𐰠'),
    'n': ('𐰣', '𐰤'),
    'r': ('𐰺', '𐰼'),
    's': ('𐰽', '𐰾'),
    't': ('𐱃', '𐱅'),
    'y': ('𐰖', '𐰘'),
}

# Neutral consonants
CONSONANTS_NEUTRAL = {
    'ç': '𐰲',
    'm': '𐰢',
    'p': '𐰯',
    'ş': '𐱁',
    'z': '𐰔',
    # Foreign/Approximations (Aggressive mapping from reference)
    'v': '𐰉', 
    'f': '𐰯', 
    'h': '𐰴', 
    'c': '𐰲', 
    'j': '𐰲',
    'w': '𐰉',
    'x': '𐰴',
    'q': '𐰴',
}

# Punctuation
# Punctuation
# We preserve punctuation by default now, so this can be empty or contain specific Göktürk punctuation if needed.
PUNCTUATION = {
    '\n': '\n',
}
