# file py_backwards/utils/tree.py:65-74
# lines [65, 68, 70, 71, 73, 74]
# branches ['70->71', '73->70', '73->74']

import ast
import pytest
from py_backwards.utils.tree import get_closest_parent_of, get_parent

# Mocking the get_parent function to control the parent lookup
@pytest.fixture
def mock_get_parent(mocker):
    return mocker.patch('py_backwards.utils.tree.get_parent')

# Test function to cover the missing lines/branches
def test_get_closest_parent_of(mock_get_parent):
    # Create a simple AST tree
    node = ast.parse("x = 1").body[0]  # Assign node
    target_type = ast.Assign

    # Setup the mock to return different types of nodes
    mock_get_parent.side_effect = [
        ast.Expr(),  # First parent (not an Assign)
        ast.Assign(),  # Second parent (is an Assign)
    ]

    # Call the function under test
    closest_parent = get_closest_parent_of(ast.AST(), node, target_type)

    # Assertions to verify the postconditions
    assert isinstance(closest_parent, target_type)
    assert isinstance(closest_parent, ast.Assign)
    # Ensure that get_parent was called twice
    assert mock_get_parent.call_count == 2
