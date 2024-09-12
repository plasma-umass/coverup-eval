# file: f064/__init__.py:1-7
# asked: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import pytest
from f064 import vowels_count

def test_vowels_count_all_vowels():
    assert vowels_count("aeiou") == 5

def test_vowels_count_no_vowels():
    assert vowels_count("bcdfg") == 0

def test_vowels_count_with_y_at_end():
    assert vowels_count("happy") == 2

def test_vowels_count_with_Y_at_end():
    assert vowels_count("HappY") == 2

def test_vowels_count_mixed_case():
    assert vowels_count("aEiOu") == 5

def test_vowels_count_empty_string():
    with pytest.raises(IndexError):
        vowels_count("")

def test_vowels_count_y_not_at_end():
    assert vowels_count("yellow") == 2

def test_vowels_count_Y_not_at_end():
    assert vowels_count("YELLOW") == 2
