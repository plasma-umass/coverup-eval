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

    @pytest.fixture
    def import_node(self):
        return ast.Import(names=[ast.alias(name='old_module', asname=None)])

    def test_visit_import_with_rewrite(self, transformer, import_node, mocker):
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=('old_module', 'new_module'))
        mocker.patch.object(transformer, '_replace_import', return_value=ast.Try(body=[], handlers=[], orelse=[], finalbody=[]))

        result = transformer.visit_Import(import_node)

        transformer._get_matched_rewrite.assert_called_once_with('old_module')
        transformer._replace_import.assert_called_once_with(import_node, 'old_module', 'new_module')
        assert isinstance(result, ast.Try)

    def test_visit_import_without_rewrite(self, transformer, import_node, mocker):
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=None)
        mocker.patch.object(transformer, 'generic_visit', return_value=import_node)

        result = transformer.visit_Import(import_node)

        transformer._get_matched_rewrite.assert_called_once_with('old_module')
        transformer.generic_visit.assert_called_once_with(import_node)
        assert result is import_node
