# file: pymonet/semigroups.py:1-21
# asked: {"lines": [1, 2, 10, 11, 13, 14, 16, 17, 19, 20, 21], "branches": []}
# gained: {"lines": [1, 2, 10, 11, 13, 14, 16, 17, 19, 20], "branches": []}

import pytest
from pymonet.semigroups import Semigroup

def test_semigroup_init():
    value = 10
    semigroup = Semigroup(value)
    assert semigroup.value == value

def test_semigroup_eq():
    value1 = 10
    value2 = 20
    semigroup1 = Semigroup(value1)
    semigroup2 = Semigroup(value1)
    semigroup3 = Semigroup(value2)
    assert semigroup1 == semigroup2
    assert semigroup1 != semigroup3

def test_semigroup_fold():
    value = 10
    semigroup = Semigroup(value)
    result = semigroup.fold(lambda x: x * 2)
    assert result == value * 2

def test_semigroup_neutral(monkeypatch):
    class SemigroupWithNeutral(Semigroup):
        neutral_element = 0

        @classmethod
        def neutral(cls):
            return cls(cls.neutral_element)

    monkeypatch.setattr(Semigroup, 'neutral', SemigroupWithNeutral.neutral)
    neutral_semigroup = Semigroup.neutral()
    assert neutral_semigroup.value == SemigroupWithNeutral.neutral_element
