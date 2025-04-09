# file src/blib2to3/pytree.py:113-119
# lines [113, 119]
# branches []

import pytest
from blib2to3.pytree import Base

class ConcreteBase(Base):
    def clone(self):
        return ConcreteBase()

def test_base_clone_not_implemented():
    concrete_instance = ConcreteBase()
    with pytest.raises(NotImplementedError):
        super(ConcreteBase, concrete_instance).clone()
