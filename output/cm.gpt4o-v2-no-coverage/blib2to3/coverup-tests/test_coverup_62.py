# file: src/blib2to3/pytree.py:345-353
# asked: {"lines": [345, 350, 351, 352, 353], "branches": []}
# gained: {"lines": [345, 350, 351, 352, 353], "branches": []}

import pytest
from blib2to3.pytree import Node, Base

class MockChild(Base):
    def __init__(self):
        self.parent = None

    def _eq(self, other):
        return self is other

def test_insert_child():
    # Arrange
    parent_node = Node(type=256, children=[])
    child_node = MockChild()
    
    # Act
    parent_node.insert_child(0, child_node)
    
    # Assert
    assert child_node.parent == parent_node
    assert parent_node.children[0] == child_node
    assert parent_node.prev_sibling_map is None
    assert parent_node.next_sibling_map is None

    # Cleanup
    parent_node.children.remove(child_node)
    child_node.parent = None
