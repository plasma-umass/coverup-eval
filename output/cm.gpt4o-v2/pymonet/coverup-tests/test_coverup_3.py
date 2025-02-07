# file: pymonet/semigroups.py:84-99
# asked: {"lines": [84, 85, 89, 90, 92, 99], "branches": []}
# gained: {"lines": [84, 85, 89, 90, 92, 99], "branches": []}

import pytest
from pymonet.semigroups import First

def test_first_str():
    first_instance = First(10)
    assert str(first_instance) == 'Fist[value=10]'

def test_first_concat():
    first_instance1 = First(10)
    first_instance2 = First(20)
    result = first_instance1.concat(first_instance2)
    assert isinstance(result, First)
    assert result.value == 10
