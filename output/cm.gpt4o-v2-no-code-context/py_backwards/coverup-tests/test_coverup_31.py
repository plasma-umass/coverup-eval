# file: py_backwards/transformers/yield_from.py:78-81
# asked: {"lines": [78, 79, 80, 81], "branches": []}
# gained: {"lines": [78, 79, 80, 81], "branches": []}

import ast
import pytest
from py_backwards.transformers.yield_from import YieldFromTransformer
from py_backwards.transformers.base import BaseNodeTransformer

class MockBaseNodeTransformer(BaseNodeTransformer):
    def __init__(self):
        pass

class MockYieldFromTransformer(YieldFromTransformer, MockBaseNodeTransformer):
    pass

class TestYieldFromTransformer:
    @pytest.fixture
    def transformer(self):
        return MockYieldFromTransformer()

    def test_visit_assignments(self, transformer, mocker):
        node = ast.parse("a = yield from b")
        mock_handle_assignments = mocker.patch.object(transformer, '_handle_assignments', return_value=node)
        mock_handle_expressions = mocker.patch.object(transformer, '_handle_expressions', return_value=node)
        mock_generic_visit = mocker.patch.object(transformer, 'generic_visit', return_value=node)

        result = transformer.visit(node)

        mock_handle_assignments.assert_called_once_with(node)
        mock_handle_expressions.assert_called_once_with(node)
        mock_generic_visit.assert_called_once_with(node)
        assert result == node

    def test_visit_expressions(self, transformer, mocker):
        node = ast.parse("yield from b")
        mock_handle_assignments = mocker.patch.object(transformer, '_handle_assignments', return_value=node)
        mock_handle_expressions = mocker.patch.object(transformer, '_handle_expressions', return_value=node)
        mock_generic_visit = mocker.patch.object(transformer, 'generic_visit', return_value=node)

        result = transformer.visit(node)

        mock_handle_assignments.assert_called_once_with(node)
        mock_handle_expressions.assert_called_once_with(node)
        mock_generic_visit.assert_called_once_with(node)
        assert result == node
