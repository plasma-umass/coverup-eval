# file: f137/__init__.py:1-10
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}

import pytest
from f137 import compare_one

def test_compare_one_integers():
    assert compare_one(1, 2) == 2
    assert compare_one(2, 1) == 2
    assert compare_one(2, 2) is None

def test_compare_one_floats():
    assert compare_one(1.0, 2.0) == 2.0
    assert compare_one(2.0, 1.0) == 2.0
    assert compare_one(2.0, 2.0) is None

def test_compare_one_strings():
    assert compare_one("1", "2") == "2"
    assert compare_one("2", "1") == "2"
    assert compare_one("2", "2") is None

def test_compare_one_strings_with_commas():
    assert compare_one("1,0", "2,0") == "2,0"
    assert compare_one("2,0", "1,0") == "2,0"
    assert compare_one("2,0", "2,0") is None

def test_compare_one_mixed():
    assert compare_one("1", 2) == 2
    assert compare_one(2, "1") == 2
    assert compare_one("2", 2) is None
