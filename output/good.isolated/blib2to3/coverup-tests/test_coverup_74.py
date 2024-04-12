# file src/blib2to3/pytree.py:287-293
# lines [287, 293]
# branches []

import pytest
from blib2to3.pytree import Node, Leaf

@pytest.fixture
def mock_children():
    # Create a list of mock children that return a string when str is called
    return [Leaf(1, "child1"), Leaf(2, "child2"), Leaf(3, "child3")]

def test_node_str(mock_children):
    node = Node(type=256, children=mock_children)  # Provide a valid type constant
    result = str(node)
    assert result == "child1child2child3", "Node __str__ did not return the correct string representation of its children"
