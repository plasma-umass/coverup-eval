# file: py_backwards/transformers/starred_unpacking.py:74-82
# asked: {"lines": [74, 75, 76, 78, 80, 81, 82], "branches": [[75, 76], [75, 78]]}
# gained: {"lines": [74, 75, 76, 78, 80, 81, 82], "branches": [[75, 76], [75, 78]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer

@pytest.fixture
def transformer():
    tree = ast.parse("")
    return StarredUnpackingTransformer(tree)

def test_visit_call_with_starred(transformer, mocker):
    node = ast.Call(
        func=ast.Name(id='print', ctx=ast.Load()),
        args=[ast.Starred(value=ast.Call(func=ast.Name(id='range', ctx=ast.Load()), args=[ast.Num(n=10)], keywords=[]), ctx=ast.Load())],
        keywords=[]
    )
    
    mocker.patch.object(transformer, '_has_starred', return_value=True)
    mocker.patch.object(transformer, '_to_sum_of_lists', return_value=ast.List(elts=[], ctx=ast.Load()))
    
    result = transformer.visit_Call(node)
    
    assert isinstance(result, ast.Call)
    assert isinstance(result.args[0], ast.Starred)
    assert transformer._tree_changed

def test_visit_call_without_starred(transformer, mocker):
    node = ast.Call(
        func=ast.Name(id='print', ctx=ast.Load()),
        args=[ast.Call(func=ast.Name(id='range', ctx=ast.Load()), args=[ast.Num(n=10)], keywords=[])],
        keywords=[]
    )
    
    mocker.patch.object(transformer, '_has_starred', return_value=False)
    
    result = transformer.visit_Call(node)
    
    assert isinstance(result, ast.Call)
    assert not transformer._tree_changed
