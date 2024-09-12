# file: f163/__init__.py:1-6
# asked: {"lines": [1, 3, 4, 6], "branches": []}
# gained: {"lines": [1, 3, 4, 6], "branches": []}

import pytest
from f163 import generate_integers

def test_generate_integers_case_1():
    result = generate_integers(1, 9)
    assert result == [2, 4, 6, 8]

def test_generate_integers_case_2():
    result = generate_integers(3, 7)
    assert result == [4, 6]

def test_generate_integers_case_3():
    result = generate_integers(2, 8)
    assert result == [2, 4, 6, 8]

def test_generate_integers_case_4():
    result = generate_integers(5, 5)
    assert result == []

def test_generate_integers_case_5():
    result = generate_integers(0, 0)
    assert result == []

def test_generate_integers_case_6():
    result = generate_integers(9, 9)
    assert result == []

def test_generate_integers_case_7():
    result = generate_integers(2, 3)
    assert result == [2]

def test_generate_integers_case_8():
    result = generate_integers(6, 8)
    assert result == [6, 8]
