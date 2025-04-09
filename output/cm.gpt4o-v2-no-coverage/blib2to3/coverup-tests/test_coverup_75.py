# file: src/blib2to3/pytree.py:224-227
# asked: {"lines": [225, 226, 227], "branches": [[225, 226], [225, 227]]}
# gained: {"lines": [225, 226, 227], "branches": [[225, 226], [225, 227]]}

import pytest
from blib2to3.pytree import Base

class MockNode(Base):
    def __init__(self, parent=None):
        self.parent = parent

def test_depth_no_parent():
    node = MockNode()
    assert node.depth() == 0

def test_depth_with_parent():
    parent_node = MockNode()
    child_node = MockNode(parent=parent_node)
    assert child_node.depth() == 1

def test_depth_with_grandparent():
    grandparent_node = MockNode()
    parent_node = MockNode(parent=grandparent_node)
    child_node = MockNode(parent=parent_node)
    assert child_node.depth() == 2
