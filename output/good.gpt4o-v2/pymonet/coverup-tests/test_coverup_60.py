# file: pymonet/utils.py:49-51
# asked: {"lines": [49, 50, 51], "branches": []}
# gained: {"lines": [49, 50, 51], "branches": []}

import pytest
from pymonet.utils import eq

def test_eq():
    assert eq(1, 1) is True
    assert eq(1, 2) is False
    assert eq("test", "test") is True
    assert eq("test", "TEST") is False

def test_curried_eq():
    curried_eq = eq(1)
    assert curried_eq(1) is True
    assert curried_eq(2) is False

    curried_eq_str = eq("test")
    assert curried_eq_str("test") is True
    assert curried_eq_str("TEST") is False
