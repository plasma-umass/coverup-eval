# file: py_backwards/transformers/python2_future.py:14-27
# asked: {"lines": [25, 26, 27], "branches": []}
# gained: {"lines": [25, 26, 27], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.python2_future import Python2FutureTransformer
from py_backwards.transformers.base import BaseNodeTransformer

@pytest.fixture
def sample_ast_module():
    return ast.Module(body=[], type_ignores=[])

def test_visit_module(sample_ast_module, mocker):
    transformer = Python2FutureTransformer(sample_ast_module)
    mocker.patch('py_backwards.transformers.python2_future.imports.get_body', return_value=[
        ast.ImportFrom(module='__future__', names=[ast.alias(name='absolute_import', asname=None)], level=0),
        ast.ImportFrom(module='__future__', names=[ast.alias(name='division', asname=None)], level=0),
        ast.ImportFrom(module='__future__', names=[ast.alias(name='print_function', asname=None)], level=0),
        ast.ImportFrom(module='__future__', names=[ast.alias(name='unicode_literals', asname=None)], level=0),
    ])
    
    result = transformer.visit_Module(sample_ast_module)
    
    assert transformer._tree_changed is True
    assert isinstance(result, ast.Module)
    assert len(result.body) == 4
    assert all(isinstance(stmt, ast.ImportFrom) for stmt in result.body)
    assert result.body[0].module == '__future__'
    assert result.body[0].names[0].name == 'absolute_import'
    assert result.body[1].names[0].name == 'division'
    assert result.body[2].names[0].name == 'print_function'
    assert result.body[3].names[0].name == 'unicode_literals'
