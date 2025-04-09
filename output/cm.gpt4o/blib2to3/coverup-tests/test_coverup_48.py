# file src/blib2to3/pytree.py:98-100
# lines [98, 99, 100]
# branches []

import pytest
from blib2to3.pytree import Base

class Derived(Base):
    @property
    def prefix(self) -> str:
        return "derived"

def test_base_prefix_not_implemented():
    derived_instance = Derived()
    with pytest.raises(NotImplementedError):
        _ = super(Derived, derived_instance).prefix
