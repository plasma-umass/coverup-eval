# file: f125/__init__.py:1-8
# asked: {"lines": [1, 3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [1, 3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

import pytest
from f125 import split_words

def test_split_words_with_space():
    result = split_words("hello world")
    assert result == ["hello", "world"]

def test_split_words_with_comma():
    result = split_words("hello,world")
    assert result == ["hello", "world"]

def test_split_words_no_space_or_comma():
    result = split_words("abcdef")
    assert result == 3  # 'b', 'd', 'f' are lowercase and have even ASCII values

def test_split_words_empty_string():
    result = split_words("")
    assert result == 0

def test_split_words_mixed_characters():
    result = split_words("aBcD")
    assert result == 0  # No lowercase characters with even ASCII values
