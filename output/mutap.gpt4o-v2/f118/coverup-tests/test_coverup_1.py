# file: f118/__init__.py:1-11
# asked: {"lines": [1, 3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}
# gained: {"lines": [1, 3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 10]]}

import pytest
from f118 import get_closest_vowel

def test_get_closest_vowel_short_word():
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("ab") == ""

def test_get_closest_vowel_no_vowel():
    assert get_closest_vowel("bcdfg") == ""

def test_get_closest_vowel_vowel_at_edges():
    assert get_closest_vowel("abca") == ""
    assert get_closest_vowel("abce") == ""

def test_get_closest_vowel_vowel_in_middle():
    assert get_closest_vowel("abec") == "e"
    assert get_closest_vowel("abic") == "i"
    assert get_closest_vowel("aboc") == "o"
    assert get_closest_vowel("abuc") == "u"

def test_get_closest_vowel_multiple_vowels():
    assert get_closest_vowel("abecid") == "i"
    assert get_closest_vowel("abicod") == "o"
    assert get_closest_vowel("abocud") == "u"
    assert get_closest_vowel("abucad") == "a"
