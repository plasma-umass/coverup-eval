# file: pymonet/semigroups.py:64-81
# asked: {"lines": [64, 65, 69, 71, 72, 74, 81], "branches": []}
# gained: {"lines": [64, 65, 69, 71, 72, 74, 81], "branches": []}

import pytest
from pymonet.semigroups import One, Semigroup

def test_one_str():
    one_instance = One(True)
    assert str(one_instance) == 'One[value=True]'
    one_instance_false = One(False)
    assert str(one_instance_false) == 'One[value=False]'

def test_one_concat():
    one_true = One(True)
    one_false = One(False)
    
    result = one_true.concat(one_false)
    assert isinstance(result, One)
    assert result.value is True
    
    result = one_false.concat(one_true)
    assert isinstance(result, One)
    assert result.value is True
    
    result = one_false.concat(one_false)
    assert isinstance(result, One)
    assert result.value is False

@pytest.fixture
def semigroup_instance():
    return Semigroup(True)

def test_one_concat_with_semigroup(semigroup_instance):
    one_instance = One(False)
    result = one_instance.concat(semigroup_instance)
    assert isinstance(result, One)
    assert result.value is True

    one_instance_true = One(True)
    result = one_instance_true.concat(semigroup_instance)
    assert isinstance(result, One)
    assert result.value is True
