# file: pymonet/semigroups.py:44-61
# asked: {"lines": [44, 45, 49, 51, 52, 54, 61], "branches": []}
# gained: {"lines": [44, 45, 49, 51, 52, 54, 61], "branches": []}

import pytest
from pymonet.semigroups import All

def test_all_str():
    all_instance = All(True)
    assert str(all_instance) == 'All[value=True]'
    all_instance_false = All(False)
    assert str(all_instance_false) == 'All[value=False]'

def test_all_concat():
    all_true = All(True)
    all_false = All(False)
    
    result = all_true.concat(all_true)
    assert result.value is True
    
    result = all_true.concat(all_false)
    assert result.value is False
    
    result = all_false.concat(all_true)
    assert result.value is False
    
    result = all_false.concat(all_false)
    assert result.value is False
