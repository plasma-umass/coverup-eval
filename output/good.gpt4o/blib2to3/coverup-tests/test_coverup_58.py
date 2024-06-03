# file src/blib2to3/pytree.py:129-135
# lines [129, 135]
# branches []

import pytest
from blib2to3.pytree import Base

class ConcreteBase(Base):
    def pre_order(self):
        return super().pre_order()

def test_base_pre_order_not_implemented():
    concrete_instance = ConcreteBase()
    with pytest.raises(NotImplementedError):
        list(concrete_instance.pre_order())
