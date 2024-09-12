# file: src/blib2to3/pytree.py:113-119
# asked: {"lines": [113, 119], "branches": []}
# gained: {"lines": [113, 119], "branches": []}

import pytest
from blib2to3.pytree import Base

class ConcreteBase(Base):
    def clone(self):
        return super().clone()

def test_base_clone_not_implemented():
    concrete_instance = ConcreteBase()
    with pytest.raises(NotImplementedError):
        concrete_instance.clone()
