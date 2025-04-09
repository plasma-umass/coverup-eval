# file: py_backwards/utils/tree.py:26-35
# asked: {"lines": [26, 29, 31, 32, 33, 35], "branches": [[31, 32], [31, 35]]}
# gained: {"lines": [26, 29, 31, 35], "branches": [[31, 35]]}

import ast
import pytest
from py_backwards.utils.tree import get_non_exp_parent_and_index, get_parent

def test_get_non_exp_parent_and_index(monkeypatch):
    class MockNode(ast.AST):
        _fields = ('body',)

    class MockParent(ast.AST):
        _fields = ('body',)
        body = [MockNode()]

    mock_node = MockNode()
    mock_parent = MockParent()
    mock_parent.body = [mock_node]

    def mock_get_parent(tree, node):
        if node is mock_node:
            return mock_parent
        return None

    monkeypatch.setattr('py_backwards.utils.tree.get_parent', mock_get_parent)

    tree = ast.Module(body=[mock_parent])
    parent, index = get_non_exp_parent_and_index(tree, mock_node)

    assert parent is mock_parent
    assert index == 0
