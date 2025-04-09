# file src/blib2to3/pytree.py:329-332
# lines [329, 330, 331, 332]
# branches ['331->exit', '331->332']

import pytest
from blib2to3.pytree import Base

class Node(Base):
    def __init__(self, children=None):
        self._prefix = ""
        self.children = children or []

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, prefix) -> None:
        self._prefix = prefix
        if self.children:
            self.children[0].prefix = prefix

def test_node_prefix_setter():
    # Create a child node
    child_node = Node()
    
    # Create a parent node with the child node
    parent_node = Node(children=[child_node])
    
    # Set the prefix of the parent node
    parent_node.prefix = "test_prefix"
    
    # Assert that the prefix of the parent node is set correctly
    assert parent_node.prefix == "test_prefix"
    
    # Assert that the prefix of the child node is also set correctly
    assert child_node.prefix == "test_prefix"
    
    # Clean up
    del parent_node
    del child_node
