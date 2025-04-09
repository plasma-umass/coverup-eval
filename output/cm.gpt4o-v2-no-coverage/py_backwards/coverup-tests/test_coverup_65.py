# file: py_backwards/transformers/base.py:75-85
# asked: {"lines": [77, 79, 80, 81, 82, 84, 85], "branches": []}
# gained: {"lines": [77, 79, 80, 81, 82, 84, 85], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.base import BaseImportRewrite

@pytest.fixture
def import_from_node():
    return ast.ImportFrom(module='old_module', names=[ast.alias(name='name', asname=None)], level=0)

def mock_get_body(previous, current):
    return [current]

def test_replace_import_from_module(import_from_node, mocker):
    transformer = BaseImportRewrite(mocker.Mock())
    mocker.patch.object(transformer, '_tree_changed', False)
    mocker.patch('py_backwards.transformers.base.import_rewrite.get_body', side_effect=mock_get_body)

    result = transformer._replace_import_from_module(import_from_node, 'old', 'new')

    assert transformer._tree_changed is True
    assert result is not None
    assert result.module == 'new_module'
    assert result.names == import_from_node.names
    assert result.level == import_from_node.level
