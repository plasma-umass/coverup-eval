# file: py_backwards/transformers/base.py:87-94
# asked: {"lines": [87, 89, 90, 91, 92, 93, 94], "branches": [[89, 0], [89, 90], [91, 89], [91, 92], [93, 89], [93, 94]]}
# gained: {"lines": [87, 89, 90, 91, 92, 93, 94], "branches": [[89, 0], [89, 90], [91, 89], [91, 92], [93, 89], [93, 94]]}

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

    def test_get_names_to_replace_with_rewrite(self, transformer, mocker):
        node = ast.ImportFrom(
            module='some_module',
            names=[ast.alias(name='some_name', asname=None)],
            level=0
        )
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=('new_module', 'new_name'))
        
        result = list(transformer._get_names_to_replace(node))
        
        assert result == [('some_module.some_name', ('new_module', 'new_name'))]

    def test_get_names_to_replace_without_rewrite(self, transformer, mocker):
        node = ast.ImportFrom(
            module='some_module',
            names=[ast.alias(name='some_name', asname=None)],
            level=0
        )
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=None)
        
        result = list(transformer._get_names_to_replace(node))
        
        assert result == []

    def test_get_names_to_replace_with_wildcard(self, transformer):
        node = ast.ImportFrom(
            module='some_module',
            names=[ast.alias(name='*', asname=None)],
            level=0
        )
        
        result = list(transformer._get_names_to_replace(node))
        
        assert result == []
