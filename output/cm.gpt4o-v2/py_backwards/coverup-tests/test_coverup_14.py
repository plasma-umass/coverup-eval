# file: py_backwards/utils/snippet.py:93-97
# asked: {"lines": [93, 94, 95, 96, 97], "branches": [[94, 0], [94, 95], [95, 94], [95, 96]]}
# gained: {"lines": [93, 94, 95, 96, 97], "branches": [[94, 0], [94, 95], [95, 96]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import extend_tree
from py_backwards.utils.tree import find, get_non_exp_parent_and_index, replace_at

class Variable:
    def __init__(self, id):
        self.id = id

def test_extend_tree(monkeypatch):
    # Create a sample AST
    tree = ast.parse("extend(x)")

    # Create a mock variable dictionary
    variables = {"x": Variable("x")}

    # Mock the find function to return the call node
    def mock_find(tree, type_):
        for node in ast.walk(tree):
            if isinstance(node, type_):
                yield node

    monkeypatch.setattr("py_backwards.utils.tree.find", mock_find)

    # Mock the get_non_exp_parent_and_index function to return a parent and index
    def mock_get_non_exp_parent_and_index(tree, node):
        return tree.body[0], 0

    monkeypatch.setattr("py_backwards.utils.tree.get_non_exp_parent_and_index", mock_get_non_exp_parent_and_index)

    # Mock the replace_at function to verify it is called correctly
    def mock_replace_at(index, parent, nodes):
        assert index == 0
        assert parent == tree.body[0]
        assert nodes == variables["x"]

    monkeypatch.setattr("py_backwards.utils.tree.replace_at", mock_replace_at)

    # Call the function under test
    extend_tree(tree, variables)
