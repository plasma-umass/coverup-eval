# file: f101/__init__.py:1-15
# asked: {"lines": [1, 3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}
# gained: {"lines": [1, 3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}

import pytest
from f101 import words_string

def test_words_string_empty():
    assert words_string('') == []

def test_words_string_no_commas():
    assert words_string('hello world') == ['hello', 'world']

def test_words_string_with_commas():
    assert words_string('hello,world') == ['hello', 'world']

def test_words_string_mixed():
    assert words_string('hello, world') == ['hello', 'world']

def test_words_string_only_commas():
    assert words_string(',,,') == []
