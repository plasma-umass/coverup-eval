# file py_backwards/transformers/base.py:68-73
# lines [68, 69, 70, 71, 73]
# branches ['70->71', '70->73']

import ast
import pytest
from py_backwards.transformers.base import BaseImportRewrite, BaseNodeTransformer

class MockBaseImportRewrite(BaseImportRewrite):
    def __init__(self):
        # Mock the BaseNodeTransformer's __init__ method
        pass

class TestBaseImportRewrite:
    @pytest.fixture
    def transformer(self):
        return MockBaseImportRewrite()

    def test_visit_import_with_rewrite(self, mocker, transformer):
        # Mock the _get_matched_rewrite method to return a rewrite tuple
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=('module', 'new_module'))
        mocker.patch.object(transformer, '_replace_import', return_value=ast.Try())

        node = ast.Import(names=[ast.alias(name='module', asname=None)])
        result = transformer.visit_Import(node)

        assert isinstance(result, ast.Try)
        transformer._get_matched_rewrite.assert_called_once_with('module')
        transformer._replace_import.assert_called_once_with(node, 'module', 'new_module')

    def test_visit_import_without_rewrite(self, mocker, transformer):
        # Mock the _get_matched_rewrite method to return None
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=None)
        mocker.patch.object(transformer, 'generic_visit', return_value=ast.Import(names=[ast.alias(name='module', asname=None)]))

        node = ast.Import(names=[ast.alias(name='module', asname=None)])
        result = transformer.visit_Import(node)

        assert isinstance(result, ast.Import)
        transformer._get_matched_rewrite.assert_called_once_with('module')
        transformer.generic_visit.assert_called_once_with(node)
