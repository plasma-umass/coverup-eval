# file: py_backwards/transformers/python2_future.py:14-27
# asked: {"lines": [14, 15, 22, 24, 25, 26, 27], "branches": []}
# gained: {"lines": [14, 15, 22, 24, 25, 26, 27], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.python2_future import Python2FutureTransformer
from py_backwards.transformers.base import BaseNodeTransformer

class MockImports:
    @staticmethod
    def get_body(future):
        return [ast.ImportFrom(module='__future__', names=[ast.alias(name='absolute_import', asname=None)], level=0),
                ast.ImportFrom(module='__future__', names=[ast.alias(name='division', asname=None)], level=0),
                ast.ImportFrom(module='__future__', names=[ast.alias(name='print_function', asname=None)], level=0),
                ast.ImportFrom(module='__future__', names=[ast.alias(name='unicode_literals', asname=None)], level=0)]

@pytest.fixture
def mock_imports(monkeypatch):
    monkeypatch.setattr('py_backwards.transformers.python2_future.imports', MockImports)

def test_visit_module(mock_imports):
    source_code = """
def foo():
    return "bar"
"""
    tree = ast.parse(source_code)
    transformer = Python2FutureTransformer(tree)
    transformer.visit_Module(tree)
    
    assert transformer._tree_changed
    assert isinstance(tree.body[0], ast.ImportFrom)
    assert tree.body[0].module == '__future__'
    assert tree.body[0].names[0].name == 'absolute_import'
    assert isinstance(tree.body[1], ast.ImportFrom)
    assert tree.body[1].module == '__future__'
    assert tree.body[1].names[0].name == 'division'
    assert isinstance(tree.body[2], ast.ImportFrom)
    assert tree.body[2].module == '__future__'
    assert tree.body[2].names[0].name == 'print_function'
    assert isinstance(tree.body[3], ast.ImportFrom)
    assert tree.body[3].module == '__future__'
    assert tree.body[3].names[0].name == 'unicode_literals'
    assert isinstance(tree.body[4], ast.FunctionDef)
    assert tree.body[4].name == 'foo'
