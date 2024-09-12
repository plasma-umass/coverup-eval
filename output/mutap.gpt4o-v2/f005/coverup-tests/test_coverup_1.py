# file: f005/__init__.py:4-17
# asked: {"lines": [4, 6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}
# gained: {"lines": [4, 6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}

import pytest
from f005 import intersperse

def test_intersperse_empty_list():
    assert intersperse([], 1) == []

def test_intersperse_single_element():
    assert intersperse([1], 0) == [1]

def test_intersperse_multiple_elements():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

def test_intersperse_with_negative_delimiter():
    assert intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]

def test_intersperse_with_zero_delimiter():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

def test_intersperse_with_large_numbers():
    assert intersperse([1000, 2000, 3000], 500) == [1000, 500, 2000, 500, 3000]
