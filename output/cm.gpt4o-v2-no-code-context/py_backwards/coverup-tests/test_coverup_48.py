# file: py_backwards/transformers/base.py:54-66
# asked: {"lines": [56, 58, 59, 61, 62, 63, 65, 66], "branches": []}
# gained: {"lines": [56, 58, 59, 61, 62, 63, 65, 66], "branches": []}

import ast
import pytest
from py_backwards.transformers.base import BaseImportRewrite
from unittest.mock import patch

class TestBaseImportRewrite:
    @patch('py_backwards.transformers.base.import_rewrite.get_body')
    def test_replace_import(self, mock_get_body):
        # Mock the get_body method to return the current node
        mock_get_body.return_value = [ast.Import(names=[ast.alias(name='new_module', asname='old_module')])]

        class MockTree:
            pass

        transformer = BaseImportRewrite(tree=MockTree())
        node = ast.Import(names=[ast.alias(name='old_module', asname=None)])
        
        result = transformer._replace_import(node, 'old_module', 'new_module')
        
        assert isinstance(result, ast.Import)
        assert result.names[0].name == 'new_module'
        assert result.names[0].asname == 'old_module'
        assert transformer._tree_changed is True
