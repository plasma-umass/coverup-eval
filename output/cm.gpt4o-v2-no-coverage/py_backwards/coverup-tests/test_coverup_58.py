# file: py_backwards/transformers/starred_unpacking.py:74-82
# asked: {"lines": [75, 76, 78, 80, 81, 82], "branches": [[75, 76], [75, 78]]}
# gained: {"lines": [75, 76, 78, 80, 81, 82], "branches": [[75, 76], [75, 78]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer
from py_backwards.transformers.base import BaseNodeTransformer

class TestStarredUnpackingTransformer:
    @pytest.fixture
    def transformer(self):
        tree = ast.parse("")
        return StarredUnpackingTransformer(tree)

    def test_visit_call_no_starred(self, transformer, mocker):
        node = ast.Call(
            func=ast.Name(id='print', ctx=ast.Load()),
            args=[ast.Constant(value=1), ast.Constant(value=2)],
            keywords=[]
        )
        mocker.patch.object(transformer, '_has_starred', return_value=False)
        result = transformer.visit_Call(node)
        assert result == node
        assert not transformer._tree_changed

    def test_visit_call_with_starred(self, transformer, mocker):
        node = ast.Call(
            func=ast.Name(id='print', ctx=ast.Load()),
            args=[ast.Starred(value=ast.Name(id='a', ctx=ast.Load()))],
            keywords=[]
        )
        mocker.patch.object(transformer, '_has_starred', return_value=True)
        mocker.patch.object(transformer, '_to_sum_of_lists', return_value=ast.List(elts=[]))
        result = transformer.visit_Call(node)
        assert isinstance(result, ast.Call)
        assert isinstance(result.args[0], ast.Starred)
        assert transformer._tree_changed
