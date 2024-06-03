# file src/blib2to3/pytree.py:295-297
# lines [295, 297]
# branches []

import pytest
from blib2to3.pytree import Base

class Node(Base):
    def __init__(self, type, children):
        self.type = type
        self.children = children

    def _eq(self, other) -> bool:
        """Compare two nodes for equality."""
        return (self.type, self.children) == (other.type, other.children)

def test_node_eq():
    node1 = Node(type='type1', children=['child1', 'child2'])
    node2 = Node(type='type1', children=['child1', 'child2'])
    node3 = Node(type='type2', children=['child1', 'child2'])
    node4 = Node(type='type1', children=['child3', 'child4'])

    assert node1._eq(node2) == True, "Nodes with same type and children should be equal"
    assert node1._eq(node3) == False, "Nodes with different types should not be equal"
    assert node1._eq(node4) == False, "Nodes with different children should not be equal"
