# file: pymonet/semigroups.py:24-41
# asked: {"lines": [24, 25, 29, 31, 32, 34, 41], "branches": []}
# gained: {"lines": [24, 25, 29, 31, 32, 34, 41], "branches": []}

import pytest
from pymonet.semigroups import Sum

def test_sum_str():
    sum_instance = Sum(5)
    assert str(sum_instance) == 'Sum[value=5]'

def test_sum_concat():
    sum1 = Sum(3)
    sum2 = Sum(7)
    result = sum1.concat(sum2)
    assert result.value == 10
    assert isinstance(result, Sum)

def test_sum_neutral_element():
    assert Sum.neutral_element == 0
