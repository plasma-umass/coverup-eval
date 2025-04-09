# file: py_backwards/transformers/six_moves.py:209-213
# asked: {"lines": [209, 210, 211, 212, 213], "branches": []}
# gained: {"lines": [209, 210, 211, 212, 213], "branches": []}

import ast
import pytest
from py_backwards.transformers.six_moves import SixMovesTransformer
from py_backwards.transformers.base import BaseImportRewrite

class TestSixMovesTransformer:
    @pytest.fixture
    def transformer(self):
        return SixMovesTransformer(ast.parse(""))

    def test_target(self, transformer):
        assert transformer.target == (2, 7)

    def test_dependencies(self, transformer):
        assert transformer.dependencies == ['six']

    def test_rewrites(self, transformer):
        rewrites = list(SixMovesTransformer.rewrites)
        assert len(rewrites) > 0
        for rewrite in rewrites:
            assert isinstance(rewrite, tuple)
            assert len(rewrite) == 2
            assert isinstance(rewrite[0], str)
            assert isinstance(rewrite[1], str)

    def test_visit_import(self, mocker, transformer):
        node = ast.Import(names=[ast.alias(name='mock', asname=None)])
        mock_get_matched_rewrite = mocker.patch.object(BaseImportRewrite, '_get_matched_rewrite', return_value=('mock', 'mock'))
        mock_replace_import = mocker.patch.object(BaseImportRewrite, '_replace_import', return_value=ast.Try(body=[], handlers=[], orelse=[], finalbody=[]))
        transformer.visit_Import(node)
        mock_get_matched_rewrite.assert_called_once_with('mock')
        mock_replace_import.assert_called_once()

    def test_visit_import_from(self, mocker, transformer):
        node = ast.ImportFrom(module='mock', names=[ast.alias(name='mock', asname=None)], level=0)
        mock_get_names_to_replace = mocker.patch.object(BaseImportRewrite, '_get_names_to_replace', return_value={'mock': ('mock', 'mock')})
        mock_replace_import_from_names = mocker.patch.object(BaseImportRewrite, '_replace_import_from_names', return_value=ast.Try(body=[], handlers=[], orelse=[], finalbody=[]))
        transformer.visit_ImportFrom(node)
        mock_get_names_to_replace.assert_called_once_with(node)
        mock_replace_import_from_names.assert_called_once()
