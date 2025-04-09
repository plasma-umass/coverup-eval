# file src/blib2to3/pytree.py:129-135
# lines [129, 135]
# branches []

import pytest
from blib2to3.pytree import Base

class ConcreteBase(Base):
    def pre_order(self):
        yield "test"

def test_concrete_base_pre_order():
    concrete_instance = ConcreteBase()
    pre_order_gen = concrete_instance.pre_order()
    assert next(pre_order_gen) == "test"
    with pytest.raises(StopIteration):
        next(pre_order_gen)
