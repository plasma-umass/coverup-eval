# file: py_backwards/utils/snippet.py:25-26
# asked: {"lines": [25, 26], "branches": []}
# gained: {"lines": [25, 26], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

class Variable:
    def __init__(self, name):
        self.name = name

@pytest.fixture
def sample_tree():
    return ast.parse("""
def foo(x):
    y = x + 1
    return y
""")

def test_replace_field_or_node():
    variables = {'x': 'z', 'y': 'w'}
    replacer = VariablesReplacer(variables)
    node = ast.Name(id='x', ctx=ast.Load())
    replaced_node = replacer._replace_field_or_node(node, 'id', True)
    assert replaced_node.id == 'z'

def test_visit_Name(sample_tree):
    variables = {'x': 'z'}
    replacer = VariablesReplacer(variables)
    replacer.visit(sample_tree)
    assert sample_tree.body[0].args.args[0].arg == 'z'

def test_visit_FunctionDef(sample_tree):
    variables = {'foo': 'bar'}
    replacer = VariablesReplacer(variables)
    replacer.visit(sample_tree)
    assert sample_tree.body[0].name == 'bar'

def test_visit_Attribute():
    variables = {'obj': ast.Name(id='new_obj', ctx=ast.Load())}
    replacer = VariablesReplacer(variables)
    node = ast.Attribute(value=ast.Name(id='obj', ctx=ast.Load()), attr='attr', ctx=ast.Load())
    replacer.visit(node)
    assert isinstance(node.value, ast.Name)
    assert node.value.id == 'new_obj'

def test_visit_keyword():
    variables = {'kw': 'new_kw'}
    replacer = VariablesReplacer(variables)
    node = ast.keyword(arg='kw', value=ast.Constant(value=1))
    replacer.visit(node)
    assert node.arg == 'new_kw'

def test_visit_ClassDef():
    variables = {'MyClass': 'NewClass'}
    replacer = VariablesReplacer(variables)
    node = ast.ClassDef(name='MyClass', bases=[], keywords=[], body=[], decorator_list=[])
    replacer.visit(node)
    assert node.name == 'NewClass'

def test_visit_arg():
    variables = {'arg': 'new_arg'}
    replacer = VariablesReplacer(variables)
    node = ast.arg(arg='arg', annotation=None)
    replacer.visit(node)
    assert node.arg == 'new_arg'

def test_replace_module():
    variables = {'module': 'new_module'}
    replacer = VariablesReplacer(variables)
    replaced_module = replacer._replace_module('module.submodule')
    assert replaced_module == 'new_module.submodule'

def test_visit_ImportFrom():
    variables = {'module': 'new_module'}
    replacer = VariablesReplacer(variables)
    node = ast.ImportFrom(module='module', names=[], level=0)
    replacer.visit(node)
    assert node.module == 'new_module'

def test_visit_alias():
    variables = {'alias': 'new_alias'}
    replacer = VariablesReplacer(variables)
    node = ast.alias(name='alias', asname=None)
    replacer.visit(node)
    assert node.name == 'new_alias'

def test_visit_ExceptHandler():
    variables = {'exc': 'new_exc'}
    replacer = VariablesReplacer(variables)
    node = ast.ExceptHandler(type=None, name='exc', body=[])
    replacer.visit(node)
    assert node.name == 'new_exc'

def test_replace(sample_tree):
    variables = {'x': 'z', 'y': 'w', 'foo': 'bar'}
    replaced_tree = VariablesReplacer.replace(sample_tree, variables)
    assert replaced_tree.body[0].name == 'bar'
    assert replaced_tree.body[0].args.args[0].arg == 'z'
    assert isinstance(replaced_tree.body[0].body[0].targets[0], ast.Name)
    assert replaced_tree.body[0].body[0].targets[0].id == 'w'
