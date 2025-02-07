# file: src/blib2to3/pytree.py:224-227
# asked: {"lines": [224, 225, 226, 227], "branches": [[225, 226], [225, 227]]}
# gained: {"lines": [224, 225, 226, 227], "branches": [[225, 226], [225, 227]]}

import pytest
from blib2to3.pytree import Base

class Node(Base):
    def __init__(self, parent=None):
        self.parent = parent

def test_depth_no_parent():
    node = Node()
    assert node.depth() == 0

def test_depth_with_parent():
    parent_node = Node()
    child_node = Node(parent=parent_node)
    assert child_node.depth() == 1

def test_depth_with_grandparent():
    grandparent_node = Node()
    parent_node = Node(parent=grandparent_node)
    child_node = Node(parent=parent_node)
    assert child_node.depth() == 2
