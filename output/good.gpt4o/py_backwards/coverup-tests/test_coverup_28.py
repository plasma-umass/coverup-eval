# file py_backwards/transformers/yield_from.py:78-81
# lines [78, 79, 80, 81]
# branches []

import ast
import pytest
from py_backwards.transformers.yield_from import YieldFromTransformer
from py_backwards.transformers.base import BaseNodeTransformer

class TestYieldFromTransformer:
    def test_visit(self, mocker):
        # Create a dummy tree to pass to the BaseNodeTransformer
        dummy_tree = ast.Module(body=[], type_ignores=[])

        # Initialize the transformer with the dummy tree
        transformer = YieldFromTransformer(dummy_tree)

        # Mock the methods _handle_assignments and _handle_expressions
        mock_handle_assignments = mocker.patch.object(transformer, '_handle_assignments', return_value=ast.Pass())
        mock_handle_expressions = mocker.patch.object(transformer, '_handle_expressions', return_value=ast.Pass())

        # Create a dummy AST node
        node = ast.Expr(value=ast.YieldFrom(value=ast.Name(id='x', ctx=ast.Load())))

        # Call the visit method
        result = transformer.visit(node)

        # Assertions to verify the methods were called and the result is as expected
        mock_handle_assignments.assert_called_once_with(node)
        mock_handle_expressions.assert_called_once_with(mock_handle_assignments.return_value)
        assert isinstance(result, ast.Pass)

        # Clean up
        mocker.stopall()
