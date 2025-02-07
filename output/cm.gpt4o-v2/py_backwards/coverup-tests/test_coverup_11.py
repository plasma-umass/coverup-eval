# file: py_backwards/utils/snippet.py:28-36
# asked: {"lines": [28, 29, 30, 31, 32, 33, 34, 36], "branches": [[30, 31], [30, 36], [31, 32], [31, 33], [33, 34], [33, 36]]}
# gained: {"lines": [28, 29, 30, 31, 32, 33, 34, 36], "branches": [[30, 31], [31, 32], [31, 33], [33, 34]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer():
    variables = {
        'a': 'b',
        'c': ast.Name(id='d', ctx=ast.Load()),
        'e': ast.Name(id='f', ctx=ast.Load())
    }
    return VariablesReplacer(variables)

def test_replace_field_or_node_string(variables_replacer):
    node = ast.Name(id='a', ctx=ast.Load())
    replaced_node = variables_replacer._replace_field_or_node(node, 'id')
    assert replaced_node.id == 'b'

def test_replace_field_or_node_same_type(variables_replacer):
    node = ast.Name(id='c', ctx=ast.Load())
    replaced_node = variables_replacer._replace_field_or_node(node, 'id')
    assert isinstance(replaced_node, ast.Name)
    assert replaced_node.id == 'd'

def test_replace_field_or_node_all_types(variables_replacer):
    node = ast.Name(id='e', ctx=ast.Load())
    replaced_node = variables_replacer._replace_field_or_node(node, 'id', all_types=True)
    assert isinstance(replaced_node, ast.Name)
    assert replaced_node.id == 'f'
