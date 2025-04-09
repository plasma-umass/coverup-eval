# file py_backwards/transformers/base.py:127-136
# lines [127, 128, 129, 130, 132, 133, 134, 136]
# branches ['129->130', '129->132', '133->134', '133->136']

import ast
import pytest
from py_backwards.transformers.base import BaseImportRewrite

class TestBaseImportRewrite:
    @pytest.fixture
    def transformer(self, mocker):
        mock_tree = mocker.Mock()
        return BaseImportRewrite(mock_tree)

    def test_visit_import_from_with_rewrite(self, mocker, transformer):
        node = ast.ImportFrom(module='some_module', names=[], level=0)
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=('new_module', 'new_name'))
        mocker.patch.object(transformer, '_replace_import_from_module', return_value=ast.ImportFrom(module='new_module', names=[], level=0))

        result = transformer.visit_ImportFrom(node)
        assert isinstance(result, ast.ImportFrom)
        assert result.module == 'new_module'

    def test_visit_import_from_with_names_to_replace(self, mocker, transformer):
        node = ast.ImportFrom(module='some_module', names=[ast.alias(name='old_name', asname=None)], level=0)
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=None)
        mocker.patch.object(transformer, '_get_names_to_replace', return_value=[('old_name', 'new_name')])
        mocker.patch.object(transformer, '_replace_import_from_names', return_value=ast.ImportFrom(module='some_module', names=[ast.alias(name='new_name', asname=None)], level=0))

        result = transformer.visit_ImportFrom(node)
        assert isinstance(result, ast.ImportFrom)
        assert result.names[0].name == 'new_name'

    def test_visit_import_from_generic_visit(self, mocker, transformer):
        node = ast.ImportFrom(module='some_module', names=[ast.alias(name='name', asname=None)], level=0)
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=None)
        mocker.patch.object(transformer, '_get_names_to_replace', return_value=[])
        mocker.patch.object(transformer, 'generic_visit', return_value=node)

        result = transformer.visit_ImportFrom(node)
        assert result == node
