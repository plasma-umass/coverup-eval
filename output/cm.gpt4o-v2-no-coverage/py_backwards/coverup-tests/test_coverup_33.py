# file: py_backwards/transformers/base.py:96-110
# asked: {"lines": [96, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110], "branches": [[100, 101], [100, 104]]}
# gained: {"lines": [96, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110], "branches": [[100, 101], [100, 104]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.base import BaseImportRewrite

class TestBaseImportRewrite:
    @pytest.fixture
    def transformer(self):
        tree = ast.Module(body=[])
        return BaseImportRewrite(tree)

    def test_get_replaced_import_from_part_no_replacement(self, transformer):
        node = ast.ImportFrom(module='os', names=[ast.alias(name='path', asname=None)], level=0)
        alias = node.names[0]
        names_to_replace = {}
        
        result = transformer._get_replaced_import_from_part(node, alias, names_to_replace)
        
        assert result.module == 'os'
        assert result.names[0].name == 'path'
        assert result.names[0].asname == 'path'
        assert result.level == 0

    def test_get_replaced_import_from_part_with_replacement(self, transformer):
        node = ast.ImportFrom(module='os', names=[ast.alias(name='path', asname=None)], level=0)
        alias = node.names[0]
        names_to_replace = {'os.path': ('os.path', 'os_new.path')}
        
        result = transformer._get_replaced_import_from_part(node, alias, names_to_replace)
        
        assert result.module == 'os_new'
        assert result.names[0].name == 'path'
        assert result.names[0].asname == 'path'
        assert result.level == 0
