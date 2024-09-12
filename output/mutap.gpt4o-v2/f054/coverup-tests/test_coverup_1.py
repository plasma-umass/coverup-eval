# file: f054/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f054 import same_chars

def test_same_chars():
    assert same_chars("abc", "bca") == True
    assert same_chars("abc", "def") == False
    assert same_chars("", "") == True
    assert same_chars("a", "a") == True
    assert same_chars("a", "b") == False
