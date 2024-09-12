# file: py_backwards/utils/snippet.py:54-56
# asked: {"lines": [54, 55, 56], "branches": []}
# gained: {"lines": [54, 55, 56], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer():
    variables = {'OldClassName': 'NewClassName'}
    replacer = VariablesReplacer(variables)
    return replacer

def test_visit_classdef_replaces_name(variables_replacer):
    class_node = ast.ClassDef(name='OldClassName', body=[], decorator_list=[])
    new_node = variables_replacer.visit_ClassDef(class_node)
    
    assert new_node.name == 'NewClassName'

def test_visit_classdef_generic_visit(variables_replacer, mocker):
    class_node = ast.ClassDef(name='OldClassName', body=[], decorator_list=[])
    mock_generic_visit = mocker.patch.object(variables_replacer, 'generic_visit', wraps=variables_replacer.generic_visit)
    
    variables_replacer.visit_ClassDef(class_node)
    
    mock_generic_visit.assert_called_once_with(class_node)
