# file: py_backwards/transformers/base.py:68-73
# asked: {"lines": [68, 69, 70, 71, 73], "branches": [[70, 71], [70, 73]]}
# gained: {"lines": [68, 69, 70, 71, 73], "branches": [[70, 71], [70, 73]]}

import pytest
import ast
from py_backwards.transformers.base import BaseImportRewrite, BaseNodeTransformer

class MockTree:
    pass

class TestBaseImportRewrite:
    @pytest.fixture
    def transformer(self):
        return BaseImportRewrite(MockTree())

    def test_visit_import_no_rewrite(self, transformer, mocker):
        # Mock the _get_matched_rewrite method to return None
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=None)
        
        # Create a simple import node
        import_node = ast.Import(names=[ast.alias(name='os', asname=None)])
        
        # Call visit_Import and assert it returns the node itself
        result = transformer.visit_Import(import_node)
        assert result == import_node

    def test_visit_import_with_rewrite(self, transformer, mocker):
        # Mock the _get_matched_rewrite method to return a tuple
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=('new_module', 'new_name'))
        
        # Mock the _replace_import method to return a new node
        new_node = ast.Import(names=[ast.alias(name='new_module', asname='new_name')])
        mocker.patch.object(transformer, '_replace_import', return_value=new_node)
        
        # Create a simple import node
        import_node = ast.Import(names=[ast.alias(name='os', asname=None)])
        
        # Call visit_Import and assert it returns the new node
        result = transformer.visit_Import(import_node)
        assert result == new_node
