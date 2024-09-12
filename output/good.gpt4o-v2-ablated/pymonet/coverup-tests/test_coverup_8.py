# file: pymonet/semigroups.py:44-61
# asked: {"lines": [44, 45, 49, 51, 52, 54, 61], "branches": []}
# gained: {"lines": [44, 45, 49, 51, 52, 54, 61], "branches": []}

import pytest
from pymonet.semigroups import All

def test_all_concat_true_true():
    a = All(True)
    b = All(True)
    result = a.concat(b)
    assert result.value is True

def test_all_concat_true_false():
    a = All(True)
    b = All(False)
    result = a.concat(b)
    assert result.value is False

def test_all_concat_false_true():
    a = All(False)
    b = All(True)
    result = a.concat(b)
    assert result.value is False

def test_all_concat_false_false():
    a = All(False)
    b = All(False)
    result = a.concat(b)
    assert result.value is False

def test_all_str():
    a = All(True)
    assert str(a) == 'All[value=True]'
    b = All(False)
    assert str(b) == 'All[value=False]'
