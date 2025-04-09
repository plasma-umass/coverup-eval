# file: pymonet/semigroups.py:24-41
# asked: {"lines": [24, 25, 29, 31, 32, 34, 41], "branches": []}
# gained: {"lines": [24, 25, 29, 31, 32, 34, 41], "branches": []}

import pytest
from pymonet.semigroups import Sum

def test_sum_concat():
    sum1 = Sum(3)
    sum2 = Sum(7)
    result = sum1.concat(sum2)
    assert result.value == 10

def test_sum_neutral_element():
    sum1 = Sum(5)
    neutral_sum = Sum(Sum.neutral_element)
    result = sum1.concat(neutral_sum)
    assert result.value == 5

def test_sum_str():
    sum1 = Sum(4)
    assert str(sum1) == 'Sum[value=4]'
