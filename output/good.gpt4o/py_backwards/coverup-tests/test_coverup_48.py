# file py_backwards/utils/tree.py:65-74
# lines [68, 70, 71, 73, 74]
# branches ['70->71', '73->70', '73->74']

import ast
import pytest
from py_backwards.utils.tree import get_closest_parent_of

def test_get_closest_parent_of(mocker):
    # Create a mock tree and nodes
    tree = ast.parse("def foo(): pass")
    node = tree.body[0]  # This is the FunctionDef node

    # Mock the get_parent function to simulate the parent traversal
    mock_get_parent = mocker.patch('py_backwards.utils.tree.get_parent')
    
    # Define a sequence of parents to return
    parent_sequence = [node, tree, None]
    mock_get_parent.side_effect = parent_sequence

    # Call the function and assert the result
    result = get_closest_parent_of(tree, node, ast.Module)
    assert result == tree

    # Ensure get_parent was called the expected number of times
    assert mock_get_parent.call_count == len(parent_sequence) - 1
