# file: f080/__init__.py:1-10
# asked: {"lines": [1, 3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}
# gained: {"lines": [1, 3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}

import pytest
from f080 import is_happy

def test_is_happy_short_string():
    assert not is_happy("ab")

def test_is_happy_no_repeats():
    assert is_happy("abc")

def test_is_happy_repeats():
    assert not is_happy("aab")
    assert not is_happy("abb")
    assert not is_happy("aba")

def test_is_happy_longer_string():
    assert is_happy("abcdef")
    assert not is_happy("abccde")
