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

def test_visit_ClassDef(variables_replacer):
    class_node = ast.ClassDef(name='OldClassName', body=[], decorator_list=[])
    new_node = variables_replacer.visit_ClassDef(class_node)
    
    assert new_node.name == 'NewClassName'
    assert isinstance(new_node, ast.ClassDef)

def test_replace_field_or_node_with_string(variables_replacer):
    class_node = ast.ClassDef(name='OldClassName', body=[], decorator_list=[])
    new_node = variables_replacer._replace_field_or_node(class_node, 'name')
    
    assert new_node.name == 'NewClassName'
    assert isinstance(new_node, ast.ClassDef)

def test_replace_field_or_node_with_node():
    variables = {'OldClassName': ast.ClassDef(name='ReplacedClass', body=[], decorator_list=[])}
    replacer = VariablesReplacer(variables)
    class_node = ast.ClassDef(name='OldClassName', body=[], decorator_list=[])
    new_node = replacer._replace_field_or_node(class_node, 'name', all_types=True)
    
    assert new_node.name == 'ReplacedClass'
    assert isinstance(new_node, ast.ClassDef)
