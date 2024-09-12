# file: f111/__init__.py:1-15
# asked: {"lines": [1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}
# gained: {"lines": [1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}

import pytest
from f111 import histogram

def test_histogram_empty_string():
    result = histogram("")
    assert result == {}

def test_histogram_single_word():
    result = histogram("word")
    assert result == {"word": 1}

def test_histogram_multiple_words():
    result = histogram("word word test test test")
    assert result == {"test": 3}

def test_histogram_no_repeated_words():
    result = histogram("one two three")
    assert result == {"one": 1, "two": 1, "three": 1}

def test_histogram_with_spaces():
    result = histogram("  word  word  test  test  test  ")
    assert result == {"test": 3}

def test_histogram_mixed_case():
    result = histogram("Word word WORD")
    assert result == {"Word": 1, "word": 1, "WORD": 1}
