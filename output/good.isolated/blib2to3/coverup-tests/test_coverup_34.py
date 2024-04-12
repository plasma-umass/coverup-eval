# file src/blib2to3/pytree.py:224-227
# lines [224, 225, 226, 227]
# branches ['225->226', '225->227']

import pytest
from blib2to3.pytree import Base

class Derived(Base):
    def __init__(self, parent=None):
        self.parent = parent

@pytest.fixture
def derived_instance():
    return Derived()

def test_derived_depth_with_no_parent(derived_instance):
    assert derived_instance.depth() == 0

def test_derived_depth_with_parent():
    parent = Derived()
    child = Derived(parent=parent)
    assert child.depth() == 1

def test_derived_depth_with_grandparent():
    grandparent = Derived()
    parent = Derived(parent=grandparent)
    child = Derived(parent=parent)
    assert child.depth() == 2
