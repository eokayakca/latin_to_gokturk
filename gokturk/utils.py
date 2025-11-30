def is_vowel(char):
    return char.lower() in "aeıioöuü"

def is_front_vowel(char):
    return char.lower() in "eiöü"

def is_back_vowel(char):
    return char.lower() in "aıou"

def get_dominant_harmony(word):
    """
    Determines if a word is predominantly back or front vowel harmony.
    Returns 'back' or 'front'. Defaults to 'back' if no vowels.
    """
    back_count = sum(1 for c in word if is_back_vowel(c))
    front_count = sum(1 for c in word if is_front_vowel(c))
    
    if front_count > back_count:
        return 'front'
    return 'back'

def get_local_harmony(word, index):
    """
    Determines the harmony for a consonant at a specific index based on the nearest vowel.
    Prioritizes the following vowel (onset rule) if equidistant.
    """
    word_len = len(word)
    
    # Search forward
    dist_fwd = float('inf')
    vowel_fwd = None
    for i in range(index + 1, word_len):
        if is_vowel(word[i]):
            dist_fwd = i - index
            vowel_fwd = word[i]
            break
            
    # Search backward
    dist_bwd = float('inf')
    vowel_bwd = None
    for i in range(index - 1, -1, -1):
        if is_vowel(word[i]):
            dist_bwd = index - i
            vowel_bwd = word[i]
            break
            
    # Decide
    target_vowel = None
    if dist_fwd < dist_bwd:
        target_vowel = vowel_fwd
    elif dist_bwd < dist_fwd:
        target_vowel = vowel_bwd
    else:
        # Tie or neither found
        if vowel_fwd: # Tie, prefer forward
            target_vowel = vowel_fwd
        elif vowel_bwd: # Only backward found (end of word)
            target_vowel = vowel_bwd
            
    if target_vowel:
        if is_front_vowel(target_vowel):
            return 'front'
        else:
            return 'back'
            
    # Fallback to dominant harmony if no vowels found nearby (e.g. word with no vowels?)
    return get_dominant_harmony(word)
