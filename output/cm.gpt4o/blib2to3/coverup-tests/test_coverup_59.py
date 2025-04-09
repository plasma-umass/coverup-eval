# file src/blib2to3/pytree.py:102-111
# lines [102, 111]
# branches []

import pytest
from blib2to3.pytree import Base

class ConcreteBase(Base):
    def _eq(self, other):
        return True

def test_base_eq_not_implemented():
    concrete_instance = ConcreteBase()
    with pytest.raises(NotImplementedError):
        super(ConcreteBase, concrete_instance)._eq(concrete_instance)
