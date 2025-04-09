# file: pymonet/utils.py:49-51
# asked: {"lines": [49, 50, 51], "branches": []}
# gained: {"lines": [49, 50, 51], "branches": []}

import pytest
from pymonet.utils import eq

def test_eq():
    assert eq(1)(1) == True
    assert eq(1)(2) == False
    assert eq('a')('a') == True
    assert eq('a')('b') == False
