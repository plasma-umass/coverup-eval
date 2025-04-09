# file: py_backwards/transformers/base.py:127-136
# asked: {"lines": [130, 136], "branches": [[129, 130], [133, 136]]}
# gained: {"lines": [130, 136], "branches": [[129, 130], [133, 136]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.base import BaseImportRewrite

class TestBaseImportRewrite:
    
    @pytest.fixture
    def transformer(self):
        tree = ast.Module(body=[])
        return BaseImportRewrite(tree)

    def test_visit_ImportFrom_with_matched_rewrite(self, transformer, mocker):
        node = ast.ImportFrom(module='old_module', names=[], level=0)
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=('old_module', 'new_module'))
        mocker.patch.object(transformer, '_replace_import_from_module', return_value='rewritten_node')
        
        result = transformer.visit_ImportFrom(node)
        
        transformer._get_matched_rewrite.assert_called_once_with('old_module')
        transformer._replace_import_from_module.assert_called_once_with(node, 'old_module', 'new_module')
        assert result == 'rewritten_node'

    def test_visit_ImportFrom_with_names_to_replace(self, transformer, mocker):
        node = ast.ImportFrom(module='module', names=[ast.alias(name='name', asname=None)], level=0)
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=None)
        mocker.patch.object(transformer, '_get_names_to_replace', return_value=[('module.name', ('module', 'new_module'))])
        mocker.patch.object(transformer, '_replace_import_from_names', return_value='rewritten_node')
        
        result = transformer.visit_ImportFrom(node)
        
        transformer._get_matched_rewrite.assert_called_once_with('module')
        transformer._get_names_to_replace.assert_called_once_with(node)
        transformer._replace_import_from_names.assert_called_once_with(node, {'module.name': ('module', 'new_module')})
        assert result == 'rewritten_node'

    def test_visit_ImportFrom_with_generic_visit(self, transformer, mocker):
        node = ast.ImportFrom(module='module', names=[ast.alias(name='name', asname=None)], level=0)
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=None)
        mocker.patch.object(transformer, '_get_names_to_replace', return_value=[])
        mocker.patch.object(transformer, 'generic_visit', return_value='generic_visit_node')
        
        result = transformer.visit_ImportFrom(node)
        
        transformer._get_matched_rewrite.assert_called_once_with('module')
        transformer._get_names_to_replace.assert_called_once_with(node)
        transformer.generic_visit.assert_called_once_with(node)
        assert result == 'generic_visit_node'
