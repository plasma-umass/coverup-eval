# file src/blib2to3/pytree.py:86-94
# lines [86, 92, 93, 94]
# branches ['92->93', '92->94']

import pytest
from blib2to3.pytree import Base

class MockBase(Base):
    def _eq(self, other):
        return True

@pytest.fixture
def cleanup():
    # Setup if necessary
    yield
    # Cleanup if necessary

def test_base_eq(cleanup):
    # Create two instances of MockBase
    base1 = MockBase()
    base2 = MockBase()
    
    # Test equality with the same class
    assert base1 == base2
    
    # Test equality with different class
    class OtherClass:
        pass
    
    other = OtherClass()
    assert (base1 == other) is False
    
    # Cleanup is handled by the fixture
