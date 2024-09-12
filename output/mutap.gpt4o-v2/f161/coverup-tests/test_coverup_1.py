# file: f161/__init__.py:1-16
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}

import pytest
from f161 import solve

def test_solve_all_alpha():
    result = solve("HelloWorld")
    assert result == "hELLOwORLD"

def test_solve_no_alpha():
    result = solve("12345")
    assert result == "54321"

def test_solve_mixed():
    result = solve("Hello123")
    assert result == "hELLO123"

def test_solve_empty():
    result = solve("")
    assert result == ""

def test_solve_special_chars():
    result = solve("!@#")
    assert result == "#@!"

