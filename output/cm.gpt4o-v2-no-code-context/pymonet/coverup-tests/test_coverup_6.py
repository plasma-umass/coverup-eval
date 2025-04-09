# file: pymonet/semigroups.py:160-177
# asked: {"lines": [160, 161, 165, 167, 168, 170, 177], "branches": []}
# gained: {"lines": [160, 161, 165, 167, 168, 170, 177], "branches": []}

import pytest
from pymonet.semigroups import Min

def test_min_concat():
    min1 = Min(10)
    min2 = Min(20)
    result = min1.concat(min2)
    assert result.value == 10

    min3 = Min(5)
    result = min1.concat(min3)
    assert result.value == 5

def test_min_str():
    min1 = Min(10)
    assert str(min1) == 'Min[value=10]'

def test_min_neutral_element():
    assert Min.neutral_element == float("inf")
