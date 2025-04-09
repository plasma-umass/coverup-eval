# file pymonet/semigroups.py:84-99
# lines [84, 85, 89, 90, 92, 99]
# branches []

import pytest
from pymonet.semigroups import First

def test_first_str_representation():
    first_instance = First('test_value')
    assert str(first_instance) == 'Fist[value=test_value]'

def test_first_concat():
    first_instance1 = First('value1')
    first_instance2 = First('value2')
    result = first_instance1.concat(first_instance2)
    assert isinstance(result, First)
    assert result.value == 'value1'
