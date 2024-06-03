# file py_backwards/transformers/base.py:17-29
# lines [17, 18, 20, 21, 22, 23, 25, 26, 27, 28, 29]
# branches []

import ast
import pytest
from py_backwards.transformers.base import BaseNodeTransformer, TransformationResult

class TestBaseNodeTransformer:
    def test_transform(self):
        # Create a simple AST node
        tree = ast.parse("x = 1")
        
        # Transform the tree using the BaseNodeTransformer
        result = BaseNodeTransformer.transform(tree)
        
        # Verify the result is a TransformationResult instance
        assert isinstance(result, TransformationResult)
        
        # Verify the tree in the result is the same as the input tree
        assert result.tree == tree
        
        # Verify the tree_changed flag is False (since no changes are made in BaseNodeTransformer)
        assert result.tree_changed is False
        
        # Verify the dependencies are an empty list
        assert result.dependencies == []
