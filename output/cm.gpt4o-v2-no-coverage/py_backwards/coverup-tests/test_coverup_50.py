# file: py_backwards/utils/snippet.py:50-52
# asked: {"lines": [50, 51, 52], "branches": []}
# gained: {"lines": [50, 51, 52], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer():
    variables = {'arg': 'replaced_arg'}
    replacer = VariablesReplacer(variables)
    return replacer

def test_visit_keyword(variables_replacer):
    node = ast.keyword(arg='arg', value=ast.Constant(value=42))
    replaced_node = variables_replacer.visit_keyword(node)
    
    assert replaced_node.arg == 'replaced_arg'
    assert isinstance(replaced_node.value, ast.Constant)
    assert replaced_node.value.value == 42

def test_replace_field_or_node_with_string(variables_replacer):
    node = ast.keyword(arg='arg', value=ast.Constant(value=42))
    replaced_node = variables_replacer._replace_field_or_node(node, 'arg')
    
    assert replaced_node.arg == 'replaced_arg'

def test_replace_field_or_node_with_node(variables_replacer):
    variables_replacer._variables = {'arg': ast.keyword(arg='new_arg', value=ast.Constant(value=99))}
    node = ast.keyword(arg='arg', value=ast.Constant(value=42))
    replaced_node = variables_replacer._replace_field_or_node(node, 'arg', all_types=True)
    
    assert replaced_node.arg == 'new_arg'
    assert replaced_node.value.value == 99
