# file src/blib2to3/pytree.py:113-119
# lines [119]
# branches []

import pytest
from blib2to3.pytree import Base

class ConcreteBase(Base):
    def clone(self):
        return super().clone()

def test_base_clone_not_implemented():
    with pytest.raises(NotImplementedError):
        ConcreteBase().clone()
