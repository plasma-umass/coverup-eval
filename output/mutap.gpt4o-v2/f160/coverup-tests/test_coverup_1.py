# file: f160/__init__.py:1-6
# asked: {"lines": [1, 3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [1, 3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

import pytest

from f160 import do_algebra

def test_do_algebra_addition():
    result = do_algebra(['+'], [1, 2])
    assert result == 3

def test_do_algebra_subtraction():
    result = do_algebra(['-'], [5, 3])
    assert result == 2

def test_do_algebra_multiplication():
    result = do_algebra(['*'], [2, 3])
    assert result == 6

def test_do_algebra_division():
    result = do_algebra(['/'], [6, 2])
    assert result == 3

def test_do_algebra_multiple_operations():
    result = do_algebra(['+', '*', '-'], [1, 2, 3, 4])
    assert result == 1 + 2 * 3 - 4

def test_do_algebra_empty_operator():
    result = do_algebra([], [1])
    assert result == 1

def test_do_algebra_empty_operand():
    with pytest.raises(IndexError):
        do_algebra(['+'], [])

def test_do_algebra_invalid_operator():
    with pytest.raises(SyntaxError):
        do_algebra(['$'], [1, 2])
