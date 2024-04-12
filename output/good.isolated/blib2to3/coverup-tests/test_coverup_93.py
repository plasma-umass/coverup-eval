# file src/blib2to3/pytree.py:129-135
# lines [135]
# branches []

import pytest
from blib2to3.pytree import Base

class DerivedBase(Base):
    pass

def test_base_pre_order_not_implemented():
    derived_instance = DerivedBase()
    with pytest.raises(NotImplementedError):
        next(derived_instance.pre_order())
