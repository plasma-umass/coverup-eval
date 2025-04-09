# file pymonet/semigroups.py:24-41
# lines [24, 25, 29, 31, 32, 34, 41]
# branches []

import pytest
from pymonet.semigroups import Sum

def test_sum_str_representation():
    sum_instance = Sum(5)
    assert str(sum_instance) == 'Sum[value=5]'

def test_sum_concat():
    sum_instance1 = Sum(5)
    sum_instance2 = Sum(10)
    result = sum_instance1.concat(sum_instance2)
    assert isinstance(result, Sum)
    assert result.value == 15
