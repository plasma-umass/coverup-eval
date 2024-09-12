# file: py_backwards/transformers/base.py:112-125
# asked: {"lines": [112, 118, 120, 121, 122, 124, 125], "branches": []}
# gained: {"lines": [112, 118, 120, 121, 122, 124, 125], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.base import BaseImportRewrite

@pytest.fixture
def mock_import_rewrite(mocker):
    return mocker.patch('py_backwards.transformers.base.import_rewrite')

def test_replace_import_from_names(mock_import_rewrite):
    tree = ast.Module(body=[])
    transformer = BaseImportRewrite(tree)
    node = ast.ImportFrom(module='module', names=[ast.alias(name='old_name', asname=None)], level=0)
    names_to_replace = {'old_name': ('new_module', 'new_name')}
    
    mock_import_rewrite.get_body.return_value = [ast.Try(body=[], handlers=[], orelse=[], finalbody=[])]
    
    result = transformer._replace_import_from_names(node, names_to_replace)
    
    assert transformer._tree_changed is True
    assert isinstance(result, ast.Try)
    mock_import_rewrite.get_body.assert_called_once()
