# file: pymonet/semigroups.py:64-81
# asked: {"lines": [64, 65, 69, 71, 72, 74, 81], "branches": []}
# gained: {"lines": [64, 65, 69, 71, 72, 74, 81], "branches": []}

import pytest
from pymonet.semigroups import One

def test_one_neutral_element():
    assert One.neutral_element == False

def test_one_str():
    one_instance = One(True)
    assert str(one_instance) == 'One[value=True]'

def test_one_concat_true_false():
    one_true = One(True)
    one_false = One(False)
    result = one_true.concat(one_false)
    assert result.value == True

def test_one_concat_false_true():
    one_false = One(False)
    one_true = One(True)
    result = one_false.concat(one_true)
    assert result.value == True

def test_one_concat_false_false():
    one_false1 = One(False)
    one_false2 = One(False)
    result = one_false1.concat(one_false2)
    assert result.value == False

def test_one_concat_true_true():
    one_true1 = One(True)
    one_true2 = One(True)
    result = one_true1.concat(one_true2)
    assert result.value == True
