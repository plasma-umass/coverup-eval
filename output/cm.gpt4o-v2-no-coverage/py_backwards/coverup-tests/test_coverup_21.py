# file: py_backwards/transformers/base.py:112-125
# asked: {"lines": [112, 118, 120, 121, 122, 124, 125], "branches": []}
# gained: {"lines": [112, 118, 120, 121, 122, 124, 125], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.base import BaseImportRewrite

class MockImportRewrite:
    @staticmethod
    def get_body(previous, current):
        return current

@pytest.fixture
def mock_import_rewrite(monkeypatch):
    monkeypatch.setattr('py_backwards.transformers.base.import_rewrite', MockImportRewrite)

def test_replace_import_from_names(mock_import_rewrite):
    node = ast.ImportFrom(module='old_module', names=[ast.alias(name='old_name', asname=None)], level=0)
    names_to_replace = {'old_module.old_name': ('old_module', 'new_module')}
    
    transformer = BaseImportRewrite(None)
    result = transformer._replace_import_from_names(node, names_to_replace)
    
    assert isinstance(result, ast.ImportFrom)
    assert result.module == 'new_module'
    assert result.names[0].name == 'old_name'
    assert result.names[0].asname == 'old_name'
