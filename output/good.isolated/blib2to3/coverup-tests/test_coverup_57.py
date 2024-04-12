# file src/blib2to3/pytree.py:102-111
# lines [102, 111]
# branches []

import pytest
from blib2to3.pytree import Base

class ConcreteBase(Base):
    def _eq(self, other):
        return super()._eq(other)  # Call the method from the Base class to raise NotImplementedError

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_base_eq_not_implemented_error(cleanup):
    concrete_instance = ConcreteBase()
    
    with pytest.raises(NotImplementedError):
        concrete_instance._eq(None)
