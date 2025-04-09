# file pymonet/semigroups.py:64-81
# lines [72, 81]
# branches []

import pytest
from pymonet.semigroups import One

def test_one_str():
    one_instance = One(False)
    one_instance.value = True
    assert str(one_instance) == 'One[value=True]'

def test_one_concat():
    one_instance1 = One(False)
    one_instance2 = One(True)
    result = one_instance1.concat(one_instance2)
    assert isinstance(result, One)
    assert result.value == True

    one_instance1 = One(False)
    one_instance2 = One(False)
    result = one_instance1.concat(one_instance2)
    assert isinstance(result, One)
    assert result.value == False
