# file: src/blib2to3/pytree.py:121-127
# asked: {"lines": [121, 127], "branches": []}
# gained: {"lines": [121, 127], "branches": []}

import pytest
from blib2to3.pytree import Base

class ConcreteBase(Base):
    def post_order(self):
        super().post_order()

def test_base_post_order_not_implemented():
    concrete_instance = ConcreteBase()
    with pytest.raises(NotImplementedError):
        list(concrete_instance.post_order())
