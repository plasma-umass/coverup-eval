# file: py_backwards/utils/snippet.py:28-36
# asked: {"lines": [28, 29, 30, 31, 32, 33, 34, 36], "branches": [[30, 31], [30, 36], [31, 32], [31, 33], [33, 34], [33, 36]]}
# gained: {"lines": [28, 29, 30, 31, 32, 33, 34, 36], "branches": [[30, 31], [30, 36], [31, 32], [31, 33], [33, 34]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

class MockNode:
    def __init__(self, field_value):
        self.field = field_value

def test_replace_field_with_string():
    variables = {'var': 'new_var'}
    replacer = VariablesReplacer(variables)
    node = MockNode('var')
    
    result = replacer._replace_field_or_node(node, 'field')
    
    assert node.field == 'new_var'
    assert result == node

def test_replace_field_with_node():
    new_node = MockNode('new_var')
    variables = {'var': new_node}
    replacer = VariablesReplacer(variables)
    node = MockNode('var')
    
    result = replacer._replace_field_or_node(node, 'field')
    
    assert result == new_node

def test_replace_field_with_node_all_types():
    new_node = MockNode('new_var')
    variables = {'var': new_node}
    replacer = VariablesReplacer(variables)
    node = MockNode('var')
    
    result = replacer._replace_field_or_node(node, 'field', all_types=True)
    
    assert result == new_node

def test_no_replacement():
    variables = {'other_var': 'new_var'}
    replacer = VariablesReplacer(variables)
    node = MockNode('var')
    
    result = replacer._replace_field_or_node(node, 'field')
    
    assert node.field == 'var'
    assert result == node
