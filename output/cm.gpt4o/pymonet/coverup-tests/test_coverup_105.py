# file pymonet/semigroups.py:102-117
# lines [108, 117]
# branches []

import pytest
from pymonet.semigroups import Last

def test_last_str():
    last_instance = Last(42)
    assert str(last_instance) == 'Last[value=42]'

def test_last_concat():
    last_instance1 = Last(42)
    last_instance2 = Last(100)
    result = last_instance1.concat(last_instance2)
    assert isinstance(result, Last)
    assert result.value == 100
