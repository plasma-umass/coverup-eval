# file: pymonet/semigroups.py:140-157
# asked: {"lines": [140, 141, 145, 147, 148, 150, 157], "branches": []}
# gained: {"lines": [140, 141, 145, 147, 148, 150, 157], "branches": []}

import pytest
from pymonet.semigroups import Max

def test_max_concat():
    max1 = Max(10)
    max2 = Max(20)
    result = max1.concat(max2)
    assert result.value == 20

    max3 = Max(30)
    result = max2.concat(max3)
    assert result.value == 30

    max4 = Max(-float("inf"))
    result = max4.concat(max1)
    assert result.value == 10

def test_max_str():
    max1 = Max(10)
    assert str(max1) == 'Max[value=10]'

def test_max_neutral_element():
    assert Max.neutral_element == -float("inf")
