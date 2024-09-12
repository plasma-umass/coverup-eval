# file: string_utils/validation.py:497-513
# asked: {"lines": [497, 510, 511, 513], "branches": [[510, 511], [510, 513]]}
# gained: {"lines": [497, 510, 511, 513], "branches": [[510, 511], [510, 513]]}

import pytest
from string_utils.validation import is_pangram

def test_is_pangram_with_pangram():
    assert is_pangram('The quick brown fox jumps over the lazy dog') == True

def test_is_pangram_with_non_pangram():
    assert is_pangram('hello world') == False

def test_is_pangram_with_empty_string():
    assert is_pangram('') == False

def test_is_pangram_with_none():
    assert is_pangram(None) == False

def test_is_pangram_with_spaces_only():
    assert is_pangram('     ') == False

def test_is_pangram_with_partial_alphabet():
    assert is_pangram('abc def ghi jkl mno pqr stu vwx yz') == True
