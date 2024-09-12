# file: f144/__init__.py:1-9
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}

import pytest
from f144 import simplify

def test_simplify_true():
    assert simplify("4/2", "2/1") == True

def test_simplify_false():
    assert simplify("2/3", "2/1") == False
