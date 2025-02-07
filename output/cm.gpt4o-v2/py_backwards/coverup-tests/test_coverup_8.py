# file: py_backwards/transformers/starred_unpacking.py:66-72
# asked: {"lines": [66, 67, 68, 70, 72], "branches": [[67, 68], [67, 70]]}
# gained: {"lines": [66, 67, 68, 70, 72], "branches": [[67, 68], [67, 70]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer

@pytest.fixture
def transformer():
    tree = ast.parse("[]")
    return StarredUnpackingTransformer(tree)

def test_visit_list_without_starred(transformer, mocker):
    node = ast.List(elts=[ast.Constant(value=1), ast.Constant(value=2)], ctx=ast.Load())
    mocker.patch.object(transformer, '_has_starred', return_value=False)
    result = transformer.visit_List(node)
    assert result == node
    assert not transformer._tree_changed

def test_visit_list_with_starred(transformer, mocker):
    node = ast.List(elts=[ast.Starred(value=ast.Name(id='a', ctx=ast.Load()), ctx=ast.Load())], ctx=ast.Load())
    mocker.patch.object(transformer, '_has_starred', return_value=True)
    mocker.patch.object(transformer, '_to_sum_of_lists', return_value=node)
    result = transformer.visit_List(node)
    assert result == node
    assert transformer._tree_changed
