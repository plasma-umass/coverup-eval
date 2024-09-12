# file: py_backwards/utils/snippet.py:46-48
# asked: {"lines": [46, 47, 48], "branches": []}
# gained: {"lines": [46, 47, 48], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer():
    variables = {'name': 'new_name'}
    replacer = VariablesReplacer(variables)
    return replacer

def test_visit_attribute_replaces_field(variables_replacer):
    class TestNode(ast.Attribute):
        def __init__(self, name):
            self.name = name

    node = TestNode(name='name')
    new_node = variables_replacer.visit_Attribute(node)
    
    assert new_node.name == 'new_name'

def test_visit_attribute_generic_visit(variables_replacer, mocker):
    class TestNode(ast.Attribute):
        def __init__(self, name):
            self.name = name

    node = TestNode(name='name')
    mocker.patch.object(variables_replacer, 'generic_visit', return_value=node)
    new_node = variables_replacer.visit_Attribute(node)
    
    variables_replacer.generic_visit.assert_called_once_with(node)
    assert new_node.name == 'new_name'
