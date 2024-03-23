# file py_backwards/transformers/base.py:112-125
# lines [112, 118, 120, 121, 122, 124, 125]
# branches []

import ast
from py_backwards.transformers.base import BaseImportRewrite
import pytest
from typed_ast import ast3

class TestBaseImportRewrite:
    @pytest.fixture
    def transformer(self, mocker):
        mocker.patch.object(BaseImportRewrite, '_get_replaced_import_from_part')
        tree = ast.parse('')
        return BaseImportRewrite(tree=tree)

    def test_replace_import_from_names(self, transformer):
        node = ast.ImportFrom(module='module', names=[ast.alias(name='name', asname=None)], level=0)
        names_to_replace = {'name': ('new_module', 'new_name')}

        result = transformer._replace_import_from_names(node, names_to_replace)

        assert isinstance(result, ast3.Try)
        transformer._get_replaced_import_from_part.assert_called_once_with(node, node.names[0], names_to_replace)
        assert transformer._tree_changed is True
