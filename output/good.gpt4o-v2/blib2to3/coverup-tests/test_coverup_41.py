# file: src/blib2to3/pytree.py:334-343
# asked: {"lines": [334, 339, 340, 341, 342, 343], "branches": []}
# gained: {"lines": [334, 339, 340, 341, 342, 343], "branches": []}

import pytest
from blib2to3.pytree import Node, Leaf

class MockChild(Leaf):
    def __init__(self):
        super().__init__(type=0, value="")
        self.parent = None

class MockNode(Node):
    def __init__(self, type, children):
        super().__init__(type, children)
        self.changed_called = False
        self.invalidate_sibling_maps_called = False

    def changed(self):
        self.changed_called = True

    def invalidate_sibling_maps(self):
        self.invalidate_sibling_maps_called = True

def test_set_child():
    # Create initial children
    child1 = MockChild()
    child2 = MockChild()
    node = MockNode(256, [child1, child2])

    # Create new child to set
    new_child = MockChild()

    # Set new child at index 1
    node.set_child(1, new_child)

    # Assertions to verify the behavior
    assert new_child.parent == node
    assert child2.parent is None
    assert node.children[1] == new_child
    assert node.changed_called
    assert node.invalidate_sibling_maps_called
