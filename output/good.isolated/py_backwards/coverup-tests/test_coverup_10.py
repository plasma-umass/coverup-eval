# file py_backwards/transformers/base.py:8-14
# lines [8, 9, 11, 12, 13, 14]
# branches []

import pytest
from py_backwards.transformers.base import BaseTransformer
from typing import NamedTuple
import ast

# Define a mock CompilationTarget for testing purposes
class MockCompilationTarget(NamedTuple):
    version: str

# Define a mock TransformationResult for testing purposes
class MockTransformationResult(NamedTuple):
    tree: ast.AST
    transformed: bool

# Define a concrete implementation of BaseTransformer for testing
class ConcreteTransformer(BaseTransformer):
    target = MockCompilationTarget(version='3.6')

    @classmethod
    def transform(cls, tree: ast.AST) -> MockTransformationResult:
        return MockTransformationResult(tree=tree, transformed=True)

# Define the test function
def test_concrete_transformer():
    # Create a simple AST node
    node = ast.parse("x = 1")

    # Transform the node using the ConcreteTransformer
    result = ConcreteTransformer.transform(node)

    # Check that the result is an instance of MockTransformationResult
    assert isinstance(result, MockTransformationResult)

    # Check that the 'transformed' attribute is True
    assert result.transformed is True

    # Check that the 'tree' attribute is the same node that was passed in
    assert result.tree is node

    # Check that the target is set correctly
    assert ConcreteTransformer.target.version == '3.6'
