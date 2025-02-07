# file: py_backwards/transformers/starred_unpacking.py:27-37
# asked: {"lines": [27, 29, 30, 31, 32, 33, 35, 36, 37], "branches": [[30, 31], [30, 37], [31, 32], [31, 35]]}
# gained: {"lines": [27, 29, 30, 31, 32, 33, 35, 36, 37], "branches": [[30, 31], [30, 37], [31, 32], [31, 35]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer

@pytest.fixture
def transformer():
    return StarredUnpackingTransformer(None)

def test_split_by_starred_with_starred(transformer):
    # Create a list of expressions with a Starred element
    exprs = [ast.Constant(value=1), ast.Starred(value=ast.Name(id='x', ctx=ast.Load())), ast.Constant(value=2)]
    
    result = transformer._split_by_starred(exprs)
    
    assert len(result) == 3
    assert isinstance(result[0], list)
    assert isinstance(result[1], ast.Starred)
    assert isinstance(result[2], list)
    assert result[0][0].value == 1
    assert result[2][0].value == 2

def test_split_by_starred_without_starred(transformer):
    # Create a list of expressions without a Starred element
    exprs = [ast.Constant(value=1), ast.Constant(value=2)]
    
    result = transformer._split_by_starred(exprs)
    
    assert len(result) == 1
    assert isinstance(result[0], list)
    assert result[0][0].value == 1
    assert result[0][1].value == 2

def test_split_by_starred_multiple_starred(transformer):
    # Create a list of expressions with multiple Starred elements
    exprs = [
        ast.Constant(value=1), 
        ast.Starred(value=ast.Name(id='x', ctx=ast.Load())), 
        ast.Constant(value=2),
        ast.Starred(value=ast.Name(id='y', ctx=ast.Load())),
        ast.Constant(value=3)
    ]
    
    result = transformer._split_by_starred(exprs)
    
    assert len(result) == 5
    assert isinstance(result[0], list)
    assert isinstance(result[1], ast.Starred)
    assert isinstance(result[2], list)
    assert isinstance(result[3], ast.Starred)
    assert isinstance(result[4], list)
    assert result[0][0].value == 1
    assert result[2][0].value == 2
    assert result[4][0].value == 3
