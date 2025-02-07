# file: src/blib2to3/pytree.py:129-135
# asked: {"lines": [129, 135], "branches": []}
# gained: {"lines": [129, 135], "branches": []}

import pytest
from blib2to3.pytree import Base

class ConcreteBase(Base):
    def pre_order(self):
        return super().pre_order()

def test_base_pre_order():
    concrete_instance = ConcreteBase()
    with pytest.raises(NotImplementedError):
        list(concrete_instance.pre_order())
