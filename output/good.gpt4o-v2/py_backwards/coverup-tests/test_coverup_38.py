# file: py_backwards/transformers/base.py:54-66
# asked: {"lines": [54, 56, 58, 59, 61, 62, 63, 65, 66], "branches": []}
# gained: {"lines": [54, 56, 58, 59, 61, 62, 63, 65, 66], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.base import BaseImportRewrite

class MockImportRewrite:
    @staticmethod
    def get_body(previous, current):
        return [current]

@pytest.fixture
def mock_import_rewrite(monkeypatch):
    monkeypatch.setattr('py_backwards.transformers.base.import_rewrite', MockImportRewrite)

def test_replace_import(mock_import_rewrite):
    tree = ast.Module(body=[])
    transformer = BaseImportRewrite(tree)
    node = ast.Import(names=[ast.alias(name='old_module', asname=None)])
    from_ = 'old'
    to = 'new'
    
    result = transformer._replace_import(node, from_, to)
    
    assert isinstance(result, ast.Import)
    assert result.names[0].name == 'new_module'
    assert result.names[0].asname == 'old_module'
    assert transformer._tree_changed
