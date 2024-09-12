# file: py_backwards/transformers/return_from_generator.py:29-54
# asked: {"lines": [43], "branches": [[42, 43]]}
# gained: {"lines": [43], "branches": [[42, 43]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.return_from_generator import ReturnFromGeneratorTransformer

@pytest.fixture
def transformer():
    return ReturnFromGeneratorTransformer(None)

def test_find_generator_returns_with_body(transformer):
    # Create a mock function node with a body that includes a node with a body and a yield statement
    node = ast.FunctionDef(
        name="test_func",
        args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
        body=[
            ast.If(
                test=ast.Name(id='x', ctx=ast.Load()),
                body=[
                    ast.Yield(value=ast.Constant(value=0)),
                    ast.Return(value=ast.Constant(value=1))
                ],
                orelse=[]
            )
        ],
        decorator_list=[]
    )

    returns = transformer._find_generator_returns(node)
    assert len(returns) == 1
    assert isinstance(returns[0][1], ast.Return)
    assert returns[0][1].value.value == 1
