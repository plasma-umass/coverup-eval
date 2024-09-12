# file: f106/__init__.py:1-13
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [5, 6], [5, 10], [7, 7], [7, 8], [11, 11], [11, 12]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [5, 6], [5, 10], [7, 7], [7, 8], [11, 11], [11, 12]]}

import pytest
from f106 import f

def test_f_even():
    result = f(4)
    assert result == [1, 2, 6, 24], f"Expected [1, 2, 6, 24] but got {result}"

def test_f_odd():
    result = f(5)
    assert result == [1, 2, 6, 24, 15], f"Expected [1, 2, 6, 24, 15] but got {result}"

def test_f_zero():
    result = f(0)
    assert result == [], f"Expected [] but got {result}"

def test_f_one():
    result = f(1)
    assert result == [1], f"Expected [1] but got {result}"
