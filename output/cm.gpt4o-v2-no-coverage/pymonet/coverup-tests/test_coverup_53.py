# file: pymonet/semigroups.py:64-81
# asked: {"lines": [64, 65, 69, 71, 72, 74, 81], "branches": []}
# gained: {"lines": [64, 65, 69, 71, 72, 74, 81], "branches": []}

import pytest
from pymonet.semigroups import One

def test_one_str():
    one_instance = One(False)
    assert str(one_instance) == 'One[value=False]'
    one_instance.value = True
    assert str(one_instance) == 'One[value=True]'

def test_one_concat():
    one_instance1 = One(False)
    one_instance2 = One(False)
    
    result = one_instance1.concat(one_instance2)
    assert isinstance(result, One)
    assert result.value == False
    
    one_instance1.value = True
    result = one_instance1.concat(one_instance2)
    assert isinstance(result, One)
    assert result.value == True
    
    one_instance1.value = False
    one_instance2.value = True
    result = one_instance1.concat(one_instance2)
    assert isinstance(result, One)
    assert result.value == True
