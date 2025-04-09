# file pymonet/semigroups.py:140-157
# lines [148, 157]
# branches []

import pytest
from pymonet.semigroups import Max

def test_max_str():
    max_instance = Max(10)
    assert str(max_instance) == 'Max[value=10]'

def test_max_concat():
    max_instance1 = Max(10)
    max_instance2 = Max(20)
    result = max_instance1.concat(max_instance2)
    assert result.value == 20

    result = max_instance2.concat(max_instance1)
    assert result.value == 20

    result = max_instance1.concat(Max(5))
    assert result.value == 10

    result = max_instance1.concat(Max(10))
    assert result.value == 10
