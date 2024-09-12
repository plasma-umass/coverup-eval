# file: py_backwards/transformers/functions_annotations.py:5-24
# asked: {"lines": [5, 6, 14, 16, 17, 18, 19, 21, 22, 23, 24], "branches": []}
# gained: {"lines": [5, 6, 14, 16, 17, 18, 19, 21, 22, 23, 24], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.functions_annotations import FunctionsAnnotationsTransformer

@pytest.fixture
def transformer():
    tree = ast.Module(body=[])
    return FunctionsAnnotationsTransformer(tree)

def test_visit_arg(transformer):
    node = ast.arg(arg='x', annotation=ast.Name(id='int', ctx=ast.Load()))
    result = transformer.visit_arg(node)
    assert transformer._tree_changed is True
    assert node.annotation is None
    assert result is node

def test_visit_FunctionDef(transformer):
    node = ast.FunctionDef(
        name='fn',
        args=ast.arguments(
            args=[ast.arg(arg='x', annotation=ast.Name(id='int', ctx=ast.Load()))],
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[]
        ),
        body=[ast.Pass()],
        decorator_list=[],
        returns=ast.Name(id='int', ctx=ast.Load())
    )
    result = transformer.visit_FunctionDef(node)
    assert transformer._tree_changed is True
    assert node.returns is None
    assert result is node
