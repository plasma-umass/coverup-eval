# file src/blib2to3/pytree.py:121-127
# lines [121, 127]
# branches []

import pytest
from blib2to3.pytree import Base

class DerivedBase(Base):
    def post_order(self):
        yield "test"

def test_derived_base_post_order():
    derived_instance = DerivedBase()
    assert next(derived_instance.post_order()) == "test"
