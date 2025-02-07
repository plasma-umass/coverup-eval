# file: src/blib2to3/pytree.py:102-111
# asked: {"lines": [102, 111], "branches": []}
# gained: {"lines": [102, 111], "branches": []}

import pytest
from blib2to3.pytree import Base

class ConcreteBase(Base):
    def _eq(self, other):
        return True

class TestBase(Base):
    def _eq(self, other):
        return super()._eq(other)

def test_base_eq_not_implemented():
    base_instance = TestBase()
    with pytest.raises(NotImplementedError):
        base_instance._eq(base_instance)

def test_concrete_base_eq():
    base_instance = ConcreteBase()
    assert base_instance._eq(base_instance) == True
