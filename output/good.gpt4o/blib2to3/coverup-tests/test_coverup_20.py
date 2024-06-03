# file src/blib2to3/pytree.py:63-80
# lines [63, 65, 75, 76, 77, 78, 79]
# branches []

import pytest
from blib2to3.pytree import Base

def test_base_class_initialization():
    # Create a subclass of Base to test instantiation
    class TestNode(Base):
        def __init__(self, type, children=None):
            self.type = type
            self.children = children if children is not None else []
    
    # Instantiate the TestNode with a type and no children
    node = TestNode(type=1)
    
    # Assertions to verify the postconditions
    assert node.type == 1
    assert node.parent is None
    assert node.children == []
    assert node.was_changed is False
    assert node.was_checked is False

    # Instantiate the TestNode with a type and some children
    children = [TestNode(type=2), TestNode(type=3)]
    node_with_children = TestNode(type=1, children=children)
    
    # Assertions to verify the postconditions
    assert node_with_children.type == 1
    assert node_with_children.parent is None
    assert node_with_children.children == children
    assert node_with_children.was_changed is False
    assert node_with_children.was_checked is False

    # Clean up
    del node
    del node_with_children
    del children

