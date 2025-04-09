# file: py_backwards/transformers/base.py:112-125
# asked: {"lines": [112, 118, 120, 121, 122, 124, 125], "branches": []}
# gained: {"lines": [112, 118, 120, 121, 122, 124, 125], "branches": []}

import ast
import pytest
from py_backwards.transformers.base import BaseImportRewrite
from py_backwards.transformers.base import BaseNodeTransformer

class MockTree:
    pass

class TestBaseImportRewrite:
    @pytest.fixture
    def transformer(self):
        return BaseImportRewrite(MockTree())

    def test_replace_import_from_names(self, transformer, mocker):
        # Create a mock node
        node = ast.ImportFrom(module='module', names=[ast.alias(name='name', asname=None)], level=0)
        
        # Mock the names_to_replace dictionary
        names_to_replace = {'name': ('old_module', 'new_module')}
        
        # Mock the _get_replaced_import_from_part method
        mocker.patch.object(transformer, '_get_replaced_import_from_part', return_value=ast.ImportFrom(module='new_module', names=[ast.alias(name='name', asname=None)], level=0))
        
        # Mock the import_rewrite.get_body method
        mock_import_rewrite_get_body = mocker.patch('py_backwards.transformers.base.import_rewrite.get_body', return_value=[ast.Try(body=[], handlers=[], orelse=[], finalbody=[])])
        
        # Call the method
        result = transformer._replace_import_from_names(node, names_to_replace)
        
        # Assertions
        assert transformer._tree_changed is True
        assert isinstance(result, ast.Try)
        mock_import_rewrite_get_body.assert_called_once()

    def test_get_replaced_import_from_part(self, transformer, mocker):
        # Create a mock node
        node = ast.ImportFrom(module='module', names=[ast.alias(name='name', asname=None)], level=0)
        
        # Mock the names_to_replace dictionary
        names_to_replace = {'name': ('old_module', 'new_module')}
        
        # Mock the _get_replaced_import_from_part method
        mocker.patch.object(transformer, '_get_replaced_import_from_part', return_value=ast.ImportFrom(module='new_module', names=[ast.alias(name='name', asname=None)], level=0))
        
        # Mock the import_rewrite.get_body method
        mock_import_rewrite_get_body = mocker.patch('py_backwards.transformers.base.import_rewrite.get_body', return_value=[ast.Try(body=[], handlers=[], orelse=[], finalbody=[])])
        
        # Call the method
        result = transformer._replace_import_from_names(node, names_to_replace)
        
        # Assertions
        assert transformer._tree_changed is True
        assert isinstance(result, ast.Try)
        mock_import_rewrite_get_body.assert_called_once()
