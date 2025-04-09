# file: py_backwards/transformers/base.py:17-29
# asked: {"lines": [17, 18, 20, 21, 22, 23, 25, 26, 27, 28, 29], "branches": []}
# gained: {"lines": [17, 18, 20, 21, 22, 23, 25, 26, 27, 28, 29], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.types import TransformationResult
from py_backwards.transformers.base import BaseNodeTransformer

class MockTransformer(BaseNodeTransformer):
    def visit(self, node):
        self._tree_changed = True

def test_base_node_transformer_init():
    tree = ast.AST()
    transformer = BaseNodeTransformer(tree)
    assert transformer._tree == tree
    assert transformer._tree_changed is False

def test_base_node_transformer_transform():
    tree = ast.AST()
    result = MockTransformer.transform(tree)
    assert isinstance(result, TransformationResult)
    assert result.tree == tree
    assert result.tree_changed is True
    assert result.dependencies == []
