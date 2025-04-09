# file: pymonet/semigroups.py:1-21
# asked: {"lines": [1, 2, 10, 11, 13, 14, 16, 17, 19, 20, 21], "branches": []}
# gained: {"lines": [1, 2, 10, 11, 13, 14, 16, 17, 19, 20, 21], "branches": []}

import pytest
from pymonet.semigroups import Semigroup

def test_semigroup_init():
    value = 5
    semigroup = Semigroup(value)
    assert semigroup.value == value

def test_semigroup_equality():
    value1 = 5
    value2 = 5
    semigroup1 = Semigroup(value1)
    semigroup2 = Semigroup(value2)
    assert semigroup1 == semigroup2

def test_semigroup_fold():
    value = 5
    semigroup = Semigroup(value)
    result = semigroup.fold(lambda x: x * 2)
    assert result == value * 2

def test_semigroup_neutral():
    class MockSemigroup(Semigroup):
        neutral_element = 0

    neutral_instance = MockSemigroup.neutral()
    assert isinstance(neutral_instance, MockSemigroup)
    assert neutral_instance.value == MockSemigroup.neutral_element
