# file: pymonet/semigroups.py:24-41
# asked: {"lines": [24, 25, 29, 31, 32, 34, 41], "branches": []}
# gained: {"lines": [24, 25, 29, 31, 32, 34, 41], "branches": []}

import pytest
from pymonet.semigroups import Sum, Semigroup

def test_sum_str():
    sum_instance = Sum(5)
    assert str(sum_instance) == 'Sum[value=5]'

def test_sum_concat():
    sum_instance1 = Sum(5)
    sum_instance2 = Sum(10)
    result = sum_instance1.concat(sum_instance2)
    assert result.value == 15
    assert isinstance(result, Sum)
