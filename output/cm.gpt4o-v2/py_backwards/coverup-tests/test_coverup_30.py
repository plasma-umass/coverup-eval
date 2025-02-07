# file: py_backwards/transformers/base.py:68-73
# asked: {"lines": [68, 69, 70, 71, 73], "branches": [[70, 71], [70, 73]]}
# gained: {"lines": [68, 69, 70, 71, 73], "branches": [[70, 71], [70, 73]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.base import BaseImportRewrite

class TestBaseImportRewrite:
    @pytest.fixture
    def transformer(self):
        tree = ast.Module(body=[])
        return BaseImportRewrite(tree)

    def test_visit_import_with_rewrite(self, transformer, mocker):
        node = ast.Import(names=[ast.alias(name='old_module', asname=None)])
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=('old_module', 'new_module'))
        mocker.patch.object(transformer, '_replace_import', return_value='rewritten_node')

        result = transformer.visit_Import(node)

        transformer._get_matched_rewrite.assert_called_once_with('old_module')
        transformer._replace_import.assert_called_once_with(node, 'old_module', 'new_module')
        assert result == 'rewritten_node'

    def test_visit_import_without_rewrite(self, transformer, mocker):
        node = ast.Import(names=[ast.alias(name='old_module', asname=None)])
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=None)
        mocker.patch.object(transformer, 'generic_visit', return_value='generic_visited_node')

        result = transformer.visit_Import(node)

        transformer._get_matched_rewrite.assert_called_once_with('old_module')
        transformer.generic_visit.assert_called_once_with(node)
        assert result == 'generic_visited_node'
