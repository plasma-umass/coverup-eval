# file: pymonet/semigroups.py:1-21
# asked: {"lines": [21], "branches": []}
# gained: {"lines": [21], "branches": []}

import pytest
from pymonet.semigroups import Semigroup

def test_semigroup_neutral():
    class TestSemigroup(Semigroup):
        neutral_element = 0

    neutral_instance = TestSemigroup.neutral()
    assert isinstance(neutral_instance, TestSemigroup)
    assert neutral_instance.value == TestSemigroup.neutral_element
