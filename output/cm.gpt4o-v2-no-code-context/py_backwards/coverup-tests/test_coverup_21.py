# file: py_backwards/transformers/return_from_generator.py:56-62
# asked: {"lines": [56, 58, 59, 61, 62], "branches": [[61, 0], [61, 62]]}
# gained: {"lines": [56, 58, 59, 61, 62], "branches": [[61, 0], [61, 62]]}

import ast
import pytest
from py_backwards.transformers.return_from_generator import ReturnFromGeneratorTransformer

class MockReturnFromGenerator:
    @staticmethod
    def get_body(return_value):
        return [ast.Expr(value=return_value)]

@pytest.fixture
def transformer(monkeypatch):
    class MockTransformer(ReturnFromGeneratorTransformer):
        def __init__(self, tree=None):
            self.tree = tree
            super().__init__(self.tree)
    
    transformer = MockTransformer()
    monkeypatch.setattr('py_backwards.transformers.return_from_generator.return_from_generator', MockReturnFromGenerator)
    return transformer

def test_replace_return(transformer):
    # Create a mock parent node with a return statement
    return_value = ast.Constant(value=42)
    return_stmt = ast.Return(value=return_value)
    parent = ast.FunctionDef(
        name="test_func",
        args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
        body=[return_stmt],
        decorator_list=[]
    )

    # Call the _replace_return method
    transformer._replace_return(parent, return_stmt)

    # Assert that the return statement was replaced
    assert len(parent.body) == 1
    assert isinstance(parent.body[0], ast.Expr)
    assert parent.body[0].value == return_value
