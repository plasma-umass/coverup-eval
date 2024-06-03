# file mimesis/random.py:65-95
# lines [93]
# branches ['90->93']

import pytest
from mimesis.random import Random

def test_custom_code_with_non_placeholder_characters():
    rnd = Random()
    mask = 'A@#B'
    char = '@'
    digit = '#'
    result = rnd.custom_code(mask=mask, char=char, digit=digit)
    
    # Ensure the result has the same length as the mask
    assert len(result) == len(mask)
    
    # Ensure the non-placeholder characters remain unchanged
    assert result[0] == 'A'
    assert result[3] == 'B'
    
    # Ensure the placeholders are replaced correctly
    assert result[1].isalpha()  # '@' should be replaced by a letter
    assert result[2].isdigit()  # '#' should be replaced by a digit
