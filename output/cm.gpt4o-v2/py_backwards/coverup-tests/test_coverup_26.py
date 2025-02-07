# file: py_backwards/transformers/base.py:87-94
# asked: {"lines": [87, 89, 90, 91, 92, 93, 94], "branches": [[89, 0], [89, 90], [91, 89], [91, 92], [93, 89], [93, 94]]}
# gained: {"lines": [87, 89, 90, 91, 92, 93, 94], "branches": [[89, 0], [89, 90], [91, 89], [91, 92], [93, 89], [93, 94]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.base import BaseImportRewrite

class TestBaseImportRewrite:
    
    @pytest.fixture
    def transformer(self):
        tree = ast.Module(body=[])
        return BaseImportRewrite(tree)

    @pytest.fixture
    def import_from_node(self):
        return ast.ImportFrom(
            module='module',
            names=[ast.alias(name='name', asname=None)],
            level=0
        )

    def test_get_names_to_replace(self, transformer, import_from_node, mocker):
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=('from', 'to'))
        
        result = list(transformer._get_names_to_replace(import_from_node))
        
        assert result == [('module.name', ('from', 'to'))]

    def test_get_names_to_replace_no_rewrite(self, transformer, import_from_node, mocker):
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=None)
        
        result = list(transformer._get_names_to_replace(import_from_node))
        
        assert result == []

    def test_get_names_to_replace_with_wildcard(self, transformer, mocker):
        import_from_node = ast.ImportFrom(
            module='module',
            names=[ast.alias(name='*', asname=None)],
            level=0
        )
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=('from', 'to'))
        
        result = list(transformer._get_names_to_replace(import_from_node))
        
        assert result == []
