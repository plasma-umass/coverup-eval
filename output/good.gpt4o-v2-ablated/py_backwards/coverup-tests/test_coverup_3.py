# file: py_backwards/utils/tree.py:26-35
# asked: {"lines": [26, 29, 31, 32, 33, 35], "branches": [[31, 32], [31, 35]]}
# gained: {"lines": [26, 29, 31, 35], "branches": [[31, 35]]}

import ast
import pytest
from py_backwards.utils.tree import get_non_exp_parent_and_index, get_parent

class MockNode(ast.AST):
    def __init__(self, body=None):
        self.body = body or []

def test_get_non_exp_parent_and_index(monkeypatch):
    # Mock get_parent to control the parent-child relationship
    def mock_get_parent(tree, node):
        if node == child_node:
            return parent_node
        elif node == parent_node:
            return grandparent_node
        return None

    monkeypatch.setattr('py_backwards.utils.tree.get_parent', mock_get_parent)

    # Create a mock AST structure
    child_node = MockNode()
    parent_node = MockNode(body=[child_node])
    grandparent_node = MockNode(body=[parent_node])

    # Call the function and assert the results
    result_parent, result_index = get_non_exp_parent_and_index(grandparent_node, child_node)
    assert result_parent == parent_node
    assert result_index == 0
