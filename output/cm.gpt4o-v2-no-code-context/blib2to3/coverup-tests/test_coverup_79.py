# file: src/blib2to3/pytree.py:177-190
# asked: {"lines": [], "branches": [[183, 190], [184, 183]]}
# gained: {"lines": [], "branches": [[183, 190]]}

import pytest
from blib2to3.pytree import Base

class MockParent:
    def __init__(self):
        self.children = []
        self.changed_called = False
        self.sibling_maps_invalidated = False

    def changed(self):
        self.changed_called = True

    def invalidate_sibling_maps(self):
        self.sibling_maps_invalidated = True

class TestBase(Base):
    def __init__(self):
        self.parent = None

@pytest.fixture
def setup_base_with_parent():
    parent = MockParent()
    base = TestBase()
    base.parent = parent
    parent.children.append(base)
    return base, parent

def test_remove_node_with_parent(setup_base_with_parent):
    base, parent = setup_base_with_parent
    position = base.remove()
    
    assert position == 0
    assert base.parent is None
    assert len(parent.children) == 0
    assert parent.changed_called
    assert parent.sibling_maps_invalidated

def test_remove_node_without_parent():
    base = TestBase()
    position = base.remove()
    
    assert position is None

def test_remove_node_not_in_parent():
    parent = MockParent()
    base = TestBase()
    base.parent = parent
    # Do not append base to parent's children
    position = base.remove()
    
    assert position is None
    assert base.parent is parent
    assert len(parent.children) == 0
    assert not parent.changed_called
    assert not parent.sibling_maps_invalidated
