# file src/blib2to3/pytree.py:81-84
# lines [81, 83, 84]
# branches []

import pytest
from blib2to3.pytree import Base

def test_base_instantiation_error():
    with pytest.raises(AssertionError) as excinfo:
        Base()
    assert str(excinfo.value) == "Cannot instantiate Base"

class Derived(Base):
    pass

def test_derived_instantiation():
    derived_instance = Derived()
    assert isinstance(derived_instance, Base)
