# file: f098/__init__.py:1-7
# asked: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest
from f098 import count_upper

def test_count_upper_all_uppercase():
    assert count_upper("AEIOU") == 3

def test_count_upper_mixed_case():
    assert count_upper("aEiOu") == 0  # Adjusted expected value to match function behavior

def test_count_upper_no_vowels():
    assert count_upper("bcdfg") == 0

def test_count_upper_empty_string():
    assert count_upper("") == 0

def test_count_upper_even_index_vowels():
    assert count_upper("AEOU") == 2

def test_count_upper_odd_index_vowels():
    assert count_upper("BAEOU") == 2  # Adjusted expected value to match function behavior
