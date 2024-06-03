# file py_backwards/utils/tree.py:58-62
# lines [58, 61, 62]
# branches []

import ast
import pytest
from py_backwards.utils.tree import replace_at

def test_replace_at(mocker):
    # Create a mock for the insert_at function
    mock_insert_at = mocker.patch('py_backwards.utils.tree.insert_at')

    # Create a parent node with a body containing some nodes
    parent = ast.Module(body=[ast.Expr(value=ast.Constant(value=1)), ast.Expr(value=ast.Constant(value=2))])

    # Define the new nodes to replace the old one
    new_nodes = ast.Expr(value=ast.Constant(value=3))

    # Call the function to test
    replace_at(0, parent, new_nodes)

    # Assert that the node at index 0 was removed
    assert len(parent.body) == 1
    assert isinstance(parent.body[0], ast.Expr)
    assert parent.body[0].value.value == 2

    # Assert that insert_at was called with the correct arguments
    mock_insert_at.assert_called_once_with(0, parent, new_nodes)
