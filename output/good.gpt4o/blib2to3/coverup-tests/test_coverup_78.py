# file src/blib2to3/pytree.py:86-94
# lines [92, 93, 94]
# branches ['92->93', '92->94']

import pytest
from blib2to3.pytree import Base

class TestBase(Base):
    def _eq(self, other):
        return True

def test_base_eq_different_class():
    base_instance = TestBase()
    other_instance = object()  # Different class instance
    assert base_instance != other_instance  # This should trigger lines 92-94

def test_base_eq_same_class():
    base_instance1 = TestBase()
    base_instance2 = TestBase()
    assert base_instance1 == base_instance2  # This should also trigger lines 92-94
