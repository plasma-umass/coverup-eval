# file: pymonet/semigroups.py:64-81
# asked: {"lines": [64, 65, 69, 71, 72, 74, 81], "branches": []}
# gained: {"lines": [64, 65, 69, 71, 72, 74, 81], "branches": []}

import pytest
from pymonet.semigroups import One

def test_one_concat_with_true_and_false():
    one_true = One(True)
    one_false = One(False)
    result = one_true.concat(one_false)
    assert result.value is True

def test_one_concat_with_false_and_true():
    one_true = One(True)
    one_false = One(False)
    result = one_false.concat(one_true)
    assert result.value is True

def test_one_concat_with_both_true():
    one_true1 = One(True)
    one_true2 = One(True)
    result = one_true1.concat(one_true2)
    assert result.value is True

def test_one_concat_with_both_false():
    one_false1 = One(False)
    one_false2 = One(False)
    result = one_false1.concat(one_false2)
    assert result.value is False

def test_one_concat_with_neutral_element():
    one_true = One(True)
    one_neutral = One(One.neutral_element)
    result = one_true.concat(one_neutral)
    assert result.value is True

def test_one_str_representation():
    one_true = One(True)
    assert str(one_true) == 'One[value=True]'
    one_false = One(False)
    assert str(one_false) == 'One[value=False]'
