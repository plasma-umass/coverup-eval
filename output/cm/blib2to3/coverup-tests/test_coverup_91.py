# file src/blib2to3/pytree.py:121-127
# lines [127]
# branches []

import pytest
from blib2to3.pytree import Base

class DerivedBase(Base):
    def post_order(self):
        return super().post_order()

def test_derived_base_post_order_not_implemented():
    derived_base_instance = DerivedBase()
    with pytest.raises(NotImplementedError):
        next(derived_base_instance.post_order())
