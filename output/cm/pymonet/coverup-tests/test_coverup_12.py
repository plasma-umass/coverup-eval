# file pymonet/semigroups.py:102-117
# lines [102, 103, 107, 108, 110, 117]
# branches []

import pytest
from pymonet.semigroups import Last

def test_last_str_representation():
    last_instance = Last(10)
    assert str(last_instance) == 'Last[value=10]'

def test_last_concat():
    last_instance1 = Last(10)
    last_instance2 = Last(20)
    result = last_instance1.concat(last_instance2)
    assert isinstance(result, Last)
    assert result.value == 20
