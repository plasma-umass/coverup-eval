# file: py_backwards/transformers/base.py:17-29
# asked: {"lines": [27, 28, 29], "branches": []}
# gained: {"lines": [27, 28, 29], "branches": []}

import ast
import pytest
from py_backwards.transformers.base import BaseNodeTransformer, TransformationResult

class TestBaseNodeTransformer:
    
    def test_transform_method(self):
        class SampleTransformer(BaseNodeTransformer):
            dependencies = ['sample_dependency']
        
        tree = ast.parse("x = 1")
        result = SampleTransformer.transform(tree)
        
        assert isinstance(result, TransformationResult)
        assert result.tree == tree
        assert result.tree_changed is False
        assert result.dependencies == ['sample_dependency']
