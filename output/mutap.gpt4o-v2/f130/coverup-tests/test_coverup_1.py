# file: f130/__init__.py:1-11
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}

import pytest
from f130 import tri

def test_tri_zero():
    assert tri(0) == [1]

def test_tri_one():
    assert tri(1) == [1, 3]

def test_tri_even():
    assert tri(2) == [1, 3, 2.0]

def test_tri_odd():
    assert tri(3) == [1, 3, 2.0, 8.0]

def test_tri_larger():
    assert tri(4) == [1, 3, 2.0, 8.0, 3.0]
