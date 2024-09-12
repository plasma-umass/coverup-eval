# file: src/blib2to3/pytree.py:81-84
# asked: {"lines": [81, 83, 84], "branches": []}
# gained: {"lines": [81, 83, 84], "branches": []}

import pytest

from blib2to3.pytree import Base

def test_base_instantiation():
    with pytest.raises(AssertionError, match="Cannot instantiate Base"):
        Base()

class Derived(Base):
    def __init__(self, value):
        self.value = value

def test_derived_instantiation():
    derived_instance = Derived(10)
    assert isinstance(derived_instance, Derived)
    assert derived_instance.value == 10
