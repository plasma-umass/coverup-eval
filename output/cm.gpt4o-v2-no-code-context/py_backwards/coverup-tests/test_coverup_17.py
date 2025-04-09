# file: py_backwards/utils/snippet.py:93-97
# asked: {"lines": [93, 94, 95, 96, 97], "branches": [[94, 0], [94, 95], [95, 94], [95, 96]]}
# gained: {"lines": [93, 94, 95], "branches": [[94, 0], [94, 95], [95, 94]]}

import ast
import pytest
from py_backwards.utils.snippet import extend_tree, find, get_non_exp_parent_and_index, replace_at, Variable

class MockVariable:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def test_extend_tree(monkeypatch):
    # Create a mock tree with a call to 'extend'
    tree = ast.parse("extend(variable_name)")

    # Mock the find function to return the call node
    def mock_find(tree, node_type):
        return [tree.body[0].value]

    monkeypatch.setattr('py_backwards.utils.snippet.find', mock_find)

    # Mock the get_non_exp_parent_and_index function to return a parent and index
    def mock_get_non_exp_parent_and_index(tree, node):
        return tree.body, 0

    monkeypatch.setattr('py_backwards.utils.snippet.get_non_exp_parent_and_index', mock_get_non_exp_parent_and_index)

    # Mock the replace_at function to verify it is called correctly
    def mock_replace_at(index, parent, variable):
        assert index == 0
        assert parent == tree.body
        assert variable.name == 'variable_name'
        assert variable.value == 'value'

    monkeypatch.setattr('py_backwards.utils.snippet.replace_at', mock_replace_at)

    # Create a variables dictionary with a MockVariable instance
    variables = {'variable_name': MockVariable(name='variable_name', value='value')}

    # Call the function under test
    extend_tree(tree, variables)
