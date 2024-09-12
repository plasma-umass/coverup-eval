# file: f010/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f010 import is_palindrome

def test_is_palindrome_true():
    assert is_palindrome("madam") == True

def test_is_palindrome_false():
    assert is_palindrome("hello") == False

def test_is_palindrome_empty_string():
    assert is_palindrome("") == True

def test_is_palindrome_single_character():
    assert is_palindrome("a") == True
