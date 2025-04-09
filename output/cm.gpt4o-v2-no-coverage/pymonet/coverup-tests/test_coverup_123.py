# file: pymonet/semigroups.py:1-21
# asked: {"lines": [21], "branches": []}
# gained: {"lines": [21], "branches": []}

import pytest
from pymonet.semigroups import Semigroup

class TestSemigroup:
    
    def test_init(self):
        value = 5
        semigroup = Semigroup(value)
        assert semigroup.value == value

    def test_eq(self):
        semigroup1 = Semigroup(5)
        semigroup2 = Semigroup(5)
        semigroup3 = Semigroup(10)
        assert semigroup1 == semigroup2
        assert semigroup1 != semigroup3

    def test_fold(self):
        semigroup = Semigroup(5)
        result = semigroup.fold(lambda x: x * 2)
        assert result == 10

    def test_neutral(self, monkeypatch):
        class MockSemigroup(Semigroup):
            neutral_element = 0

        monkeypatch.setattr(MockSemigroup, 'neutral_element', MockSemigroup.neutral_element)
        neutral_instance = MockSemigroup.neutral()
        assert isinstance(neutral_instance, Semigroup)
        assert neutral_instance.value == MockSemigroup.neutral_element
