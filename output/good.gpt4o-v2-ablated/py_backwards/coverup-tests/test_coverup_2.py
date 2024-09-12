# file: py_backwards/transformers/base.py:17-29
# asked: {"lines": [17, 18, 20, 21, 22, 23, 25, 26, 27, 28, 29], "branches": []}
# gained: {"lines": [17, 18, 20, 21, 22, 23, 25, 26, 27, 28, 29], "branches": []}

import ast
import pytest
from py_backwards.transformers.base import BaseNodeTransformer, TransformationResult

class TestBaseNodeTransformer:
    def test_init(self):
        tree = ast.parse("x = 1")
        transformer = BaseNodeTransformer(tree)
        assert transformer._tree == tree
        assert transformer._tree_changed is False

    def test_transform(self, mocker):
        tree = ast.parse("x = 1")
        mocker.patch.object(BaseNodeTransformer, 'visit', return_value=None)
        result = BaseNodeTransformer.transform(tree)
        assert isinstance(result, TransformationResult)
        assert result.tree == tree
        assert result.tree_changed is False
        assert result.dependencies == BaseNodeTransformer.dependencies
