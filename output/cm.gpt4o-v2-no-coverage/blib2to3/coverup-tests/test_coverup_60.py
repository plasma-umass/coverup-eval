# file: src/blib2to3/pytree.py:102-111
# asked: {"lines": [102, 111], "branches": []}
# gained: {"lines": [102, 111], "branches": []}

import pytest
from blib2to3.pytree import Base

class ConcreteBase(Base):
    def _eq(self, other):
        return True

def test_base_eq_not_implemented():
    class TestBase(Base):
        def _eq(self, other):
            super()._eq(other)
    
    base_instance = TestBase.__new__(TestBase)
    with pytest.raises(NotImplementedError):
        base_instance._eq(base_instance)

def test_concrete_base_eq():
    base_instance = ConcreteBase.__new__(ConcreteBase)
    assert base_instance._eq(base_instance) == True
