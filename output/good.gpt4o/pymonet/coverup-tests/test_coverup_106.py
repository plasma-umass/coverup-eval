# file pymonet/semigroups.py:160-177
# lines [168, 177]
# branches []

import pytest
from pymonet.semigroups import Min

def test_min_str():
    min_instance = Min(5)
    assert str(min_instance) == 'Min[value=5]'

def test_min_concat():
    min_instance1 = Min(5)
    min_instance2 = Min(10)
    result = min_instance1.concat(min_instance2)
    assert result.value == 5

    min_instance3 = Min(3)
    result = min_instance1.concat(min_instance3)
    assert result.value == 3
