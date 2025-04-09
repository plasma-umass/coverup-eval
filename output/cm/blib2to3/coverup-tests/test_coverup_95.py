# file src/blib2to3/pytree.py:355-363
# lines [360, 361, 362, 363]
# branches []

import pytest
from blib2to3.pytree import Node, Leaf

class TestNode:
    def test_append_child(self, mocker):
        # Create a mock for the child node with no parent attribute set
        mock_child = mocker.Mock(spec=Leaf)
        mocker.patch.object(mock_child, 'parent', None)
        # Create a Node instance with a valid type (symbol number >= 256)
        node = Node(type=256, children=[])
        # Ensure the child has no parent before appending
        assert mock_child.parent is None
        # Append the child to the node
        node.append_child(mock_child)
        # Check that the child's parent is set
        assert mock_child.parent is node
        # Check that the child is in the node's children
        assert mock_child in node.children
        # Check that the node's changed method was called
        mocker.spy(node, 'changed')
        node.append_child(mock_child)
        node.changed.assert_called_once()
        # Check that the node's invalidate_sibling_maps method was called
        mocker.spy(node, 'invalidate_sibling_maps')
        node.append_child(mock_child)
        node.invalidate_sibling_maps.assert_called_once()
