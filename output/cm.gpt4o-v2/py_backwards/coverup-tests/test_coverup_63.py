# file: py_backwards/utils/snippet.py:28-36
# asked: {"lines": [], "branches": [[33, 36]]}
# gained: {"lines": [], "branches": [[33, 36]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

class MockNode:
    def __init__(self, value):
        self.value = value

def test_replace_field_or_node_with_all_types():
    variables = {'a': MockNode('replaced')}
    replacer = VariablesReplacer(variables)
    node = MockNode('a')
    
    result = replacer._replace_field_or_node(node, 'value', all_types=True)
    
    assert result == variables['a']
    assert result.value == 'replaced'

def test_replace_field_or_node_with_matching_type():
    variables = {'a': MockNode('replaced')}
    replacer = VariablesReplacer(variables)
    node = MockNode('a')
    
    result = replacer._replace_field_or_node(node, 'value', all_types=False)
    
    assert result == variables['a']
    assert result.value == 'replaced'

def test_replace_field_or_node_with_non_matching_type():
    class DifferentNode:
        def __init__(self, value):
            self.value = value

    variables = {'a': DifferentNode('replaced')}
    replacer = VariablesReplacer(variables)
    node = MockNode('a')
    
    result = replacer._replace_field_or_node(node, 'value', all_types=False)
    
    assert result == node
    assert result.value == 'a'
