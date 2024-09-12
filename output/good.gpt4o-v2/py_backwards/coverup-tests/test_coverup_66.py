# file: py_backwards/transformers/base.py:75-85
# asked: {"lines": [77, 79, 80, 81, 82, 84, 85], "branches": []}
# gained: {"lines": [77, 79, 80, 81, 82, 84, 85], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.base import BaseImportRewrite, BaseNodeTransformer

class MockImportRewrite:
    @staticmethod
    def get_body(previous, current):
        return [ast.Try(body=[current], handlers=[], orelse=[], finalbody=[])]

@pytest.fixture
def mock_import_rewrite(monkeypatch):
    monkeypatch.setattr("py_backwards.transformers.base.import_rewrite", MockImportRewrite)

def test_replace_import_from_module(mock_import_rewrite):
    tree = ast.Module(body=[])
    transformer = BaseImportRewrite(tree)
    node = ast.ImportFrom(module="old_module", names=[], level=0)
    from_ = "old"
    to = "new"
    
    result = transformer._replace_import_from_module(node, from_, to)
    
    assert transformer._tree_changed is True
    assert isinstance(result, ast.Try)
    assert result.body[0].module == "new_module"
