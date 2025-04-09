# file src/blib2to3/pytree.py:98-100
# lines [98, 99, 100]
# branches []

import pytest
from blib2to3.pytree import Base

class Derived(Base):
    pass

def test_base_prefix_property():
    derived_instance = Derived()
    with pytest.raises(NotImplementedError):
        _ = derived_instance.prefix
