# file: pymonet/utils.py:49-51
# asked: {"lines": [49, 50, 51], "branches": []}
# gained: {"lines": [49, 50, 51], "branches": []}

import pytest
from pymonet.utils import eq

def test_eq_true():
    assert eq(5)(5) == True

def test_eq_false():
    assert eq(5)(3) == False

def test_eq_string_true():
    assert eq("test")("test") == True

def test_eq_string_false():
    assert eq("test")("fail") == False

def test_eq_list_true():
    assert eq([1, 2, 3])([1, 2, 3]) == True

def test_eq_list_false():
    assert eq([1, 2, 3])([3, 2, 1]) == False
