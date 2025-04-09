# file: py_backwards/transformers/base.py:127-136
# asked: {"lines": [127, 128, 129, 130, 132, 133, 134, 136], "branches": [[129, 130], [129, 132], [133, 134], [133, 136]]}
# gained: {"lines": [127, 128, 129, 130, 132, 133, 134, 136], "branches": [[129, 130], [129, 132], [133, 134], [133, 136]]}

import ast
import pytest
from py_backwards.transformers.base import BaseImportRewrite

class TestBaseImportRewrite:
    @pytest.fixture
    def transformer(self, mocker):
        tree = mocker.Mock()
        return BaseImportRewrite(tree)

    def test_visit_import_from_with_module_rewrite(self, transformer, mocker):
        node = ast.ImportFrom(module='some_module', names=[], level=0)
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=('new_module',))
        mocker.patch.object(transformer, '_replace_import_from_module', return_value=ast.Try())

        result = transformer.visit_ImportFrom(node)

        transformer._get_matched_rewrite.assert_called_once_with('some_module')
        transformer._replace_import_from_module.assert_called_once_with(node, 'new_module')
        assert isinstance(result, ast.Try)

    def test_visit_import_from_with_names_to_replace(self, transformer, mocker):
        node = ast.ImportFrom(module='some_module', names=[], level=0)
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=None)
        mocker.patch.object(transformer, '_get_names_to_replace', return_value=[('old_name', 'new_name')])
        mocker.patch.object(transformer, '_replace_import_from_names', return_value=ast.Try())

        result = transformer.visit_ImportFrom(node)

        transformer._get_matched_rewrite.assert_called_once_with('some_module')
        transformer._get_names_to_replace.assert_called_once_with(node)
        transformer._replace_import_from_names.assert_called_once_with(node, {'old_name': 'new_name'})
        assert isinstance(result, ast.Try)

    def test_visit_import_from_generic_visit(self, transformer, mocker):
        node = ast.ImportFrom(module='some_module', names=[], level=0)
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=None)
        mocker.patch.object(transformer, '_get_names_to_replace', return_value=[])

        result = transformer.visit_ImportFrom(node)

        transformer._get_matched_rewrite.assert_called_once_with('some_module')
        transformer._get_names_to_replace.assert_called_once_with(node)
        assert result == transformer.generic_visit(node)
