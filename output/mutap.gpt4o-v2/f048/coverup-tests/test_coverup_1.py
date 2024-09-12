# file: f048/__init__.py:1-6
# asked: {"lines": [1, 3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [1, 3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

import pytest
from f048 import is_palindrome

def test_is_palindrome_true():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("a") == True
    assert is_palindrome("") == True

def test_is_palindrome_false():
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False
    assert is_palindrome("python") == False
