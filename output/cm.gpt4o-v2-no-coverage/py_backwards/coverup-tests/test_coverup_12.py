# file: py_backwards/transformers/return_from_generator.py:56-62
# asked: {"lines": [56, 58, 59, 61, 62], "branches": [[61, 0], [61, 62]]}
# gained: {"lines": [56, 58, 59, 61, 62], "branches": [[61, 0], [61, 62]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.return_from_generator import ReturnFromGeneratorTransformer
from py_backwards.transformers.base import BaseNodeTransformer

class MockReturnFromGenerator:
    @staticmethod
    def get_body(return_value):
        exc = ast.Raise(
            exc=ast.Call(
                func=ast.Name(id='StopIteration', ctx=ast.Load()),
                args=[],
                keywords=[]
            ),
            cause=None
        )
        exc.value = return_value
        return [exc]

@pytest.fixture
def transformer(monkeypatch):
    transformer = ReturnFromGeneratorTransformer(None)
    monkeypatch.setattr('py_backwards.transformers.return_from_generator.return_from_generator', MockReturnFromGenerator)
    return transformer

def test_replace_return(transformer):
    parent = ast.FunctionDef(
        name='test_func',
        args=ast.arguments(
            args=[],
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[]
        ),
        body=[
            ast.Return(value=ast.Constant(value=5))
        ],
        decorator_list=[]
    )
    return_stmt = parent.body[0]
    transformer._replace_return(parent, return_stmt)
    
    assert len(parent.body) == 1
    assert isinstance(parent.body[0], ast.Raise)
    assert parent.body[0].exc.func.id == 'StopIteration'
    assert parent.body[0].value.value == 5
