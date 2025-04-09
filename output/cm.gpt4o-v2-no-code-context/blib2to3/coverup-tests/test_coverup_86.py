# file: src/blib2to3/pytree.py:177-190
# asked: {"lines": [], "branches": [[184, 183]]}
# gained: {"lines": [], "branches": [[184, 183]]}

import pytest
from blib2to3.pytree import Base

class MockParent:
    def __init__(self):
        self.children = []
        self.changed_called = False
        self.invalidate_sibling_maps_called = False

    def changed(self):
        self.changed_called = True

    def invalidate_sibling_maps(self):
        self.invalidate_sibling_maps_called = True

class Derived(Base):
    pass

@pytest.fixture
def setup_base_with_siblings():
    parent = MockParent()
    sibling1 = Derived()
    sibling2 = Derived()
    base = Derived()
    sibling3 = Derived()
    parent.children.extend([sibling1, sibling2, base, sibling3])
    base.parent = parent
    return base, parent

def test_remove_node_with_siblings(setup_base_with_siblings):
    base, parent = setup_base_with_siblings
    position = base.remove()
    
    assert position == 2
    assert base.parent is None
    assert len(parent.children) == 3
    assert parent.children == [parent.children[0], parent.children[1], parent.children[2]]
    assert parent.changed_called
    assert parent.invalidate_sibling_maps_called

def test_remove_node_without_parent():
    base = Derived()
    position = base.remove()
    
    assert position is None
