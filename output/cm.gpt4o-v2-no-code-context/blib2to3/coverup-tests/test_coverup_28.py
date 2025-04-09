# file: src/blib2to3/pytree.py:86-94
# asked: {"lines": [86, 92, 93, 94], "branches": [[92, 93], [92, 94]]}
# gained: {"lines": [86, 92, 93, 94], "branches": [[92, 93], [92, 94]]}

import pytest
from blib2to3.pytree import Base

class MockBase(Base):
    def _eq(self, other):
        return True

class MockDifferentBase(Base):
    def _eq(self, other):
        return False

def test_base_eq_same_class(monkeypatch):
    base1 = MockBase()
    base2 = MockBase()
    assert base1 == base2

def test_base_eq_different_class(monkeypatch):
    base1 = MockBase()
    base2 = MockDifferentBase()
    assert base1 != base2
