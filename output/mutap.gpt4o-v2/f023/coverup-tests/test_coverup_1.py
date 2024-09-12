# file: f023/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f023 import strlen

def test_strlen():
    assert strlen("test") == 4
    assert strlen("") == 0
    assert strlen("a") == 1
    assert strlen("1234567890") == 10
