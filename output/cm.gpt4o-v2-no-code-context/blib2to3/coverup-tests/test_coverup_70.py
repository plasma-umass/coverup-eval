# file: src/blib2to3/pytree.py:102-111
# asked: {"lines": [102, 111], "branches": []}
# gained: {"lines": [102, 111], "branches": []}

import pytest
from blib2to3.pytree import Base

class ConcreteBase(Base):
    def _eq(self, other):
        return True

def test_eq_not_implemented():
    class TestBase(Base):
        def __init__(self):
            pass

        def _eq(self, other):
            return super()._eq(other)

    base_instance = TestBase()
    with pytest.raises(NotImplementedError):
        base_instance._eq(base_instance)

def test_eq_implemented():
    instance1 = ConcreteBase()
    instance2 = ConcreteBase()
    assert instance1._eq(instance2) == True
