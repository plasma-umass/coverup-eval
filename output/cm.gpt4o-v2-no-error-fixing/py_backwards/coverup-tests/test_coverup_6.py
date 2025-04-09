# file: py_backwards/utils/snippet.py:28-36
# asked: {"lines": [28, 29, 30, 31, 32, 33, 34, 36], "branches": [[30, 31], [30, 36], [31, 32], [31, 33], [33, 34], [33, 36]]}
# gained: {"lines": [28, 29, 30, 31, 32, 33, 34, 36], "branches": [[30, 31], [30, 36], [31, 32], [31, 33], [33, 34]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

class MockNode:
    def __init__(self, field_value):
        self.field = field_value

@pytest.fixture
def variables_replacer():
    variables = {
        'var1': 'replacement1',
        'var2': MockNode('replacement2'),
        'var3': MockNode('replacement3')
    }
    return VariablesReplacer(variables)

def test_replace_field_with_string(variables_replacer):
    node = MockNode('var1')
    result = variables_replacer._replace_field_or_node(node, 'field')
    assert node.field == 'replacement1'
    assert result == node

def test_replace_field_with_node(variables_replacer):
    node = MockNode('var2')
    result = variables_replacer._replace_field_or_node(node, 'field')
    assert result == variables_replacer._variables['var2']

def test_replace_field_with_node_all_types(variables_replacer):
    node = MockNode('var3')
    result = variables_replacer._replace_field_or_node(node, 'field', all_types=True)
    assert result == variables_replacer._variables['var3']

def test_no_replacement(variables_replacer):
    node = MockNode('var4')
    result = variables_replacer._replace_field_or_node(node, 'field')
    assert result == node
    assert node.field == 'var4'
