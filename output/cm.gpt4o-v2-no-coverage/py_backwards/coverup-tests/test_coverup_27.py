# file: py_backwards/transformers/base.py:8-14
# asked: {"lines": [8, 9, 11, 12, 13, 14], "branches": []}
# gained: {"lines": [8, 9, 11, 12, 13], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.types import TransformationResult
from py_backwards.transformers.base import BaseTransformer

def test_base_transformer_target():
    assert BaseTransformer.target is None

def test_base_transformer_transform():
    class ConcreteTransformer(BaseTransformer):
        @classmethod
        def transform(cls, tree: ast.AST) -> TransformationResult:
            return TransformationResult(tree, False, [])

    tree = ast.parse("x = 1")
    result = ConcreteTransformer.transform(tree)
    assert isinstance(result, TransformationResult)
    assert result.tree == tree
    assert result.tree_changed is False
    assert result.dependencies == []
