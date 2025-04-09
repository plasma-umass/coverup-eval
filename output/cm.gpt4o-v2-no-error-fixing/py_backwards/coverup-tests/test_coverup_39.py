# file: py_backwards/transformers/base.py:87-94
# asked: {"lines": [89, 90, 91, 92, 93, 94], "branches": [[89, 0], [89, 90], [91, 89], [91, 92], [93, 89], [93, 94]]}
# gained: {"lines": [89, 90, 91, 92, 93, 94], "branches": [[89, 0], [89, 90], [91, 89], [91, 92], [93, 89], [93, 94]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.base import BaseImportRewrite

class MockBaseImportRewrite(BaseImportRewrite):
    def __init__(self, rewrites):
        self.rewrites = rewrites

@pytest.fixture
def mock_node():
    return ast.ImportFrom(
        module='test_module',
        names=[ast.alias(name='test_name', asname=None)],
        level=0
    )

def test_get_names_to_replace(mock_node):
    transformer = MockBaseImportRewrite(rewrites=[('test_module.test_name', 'new_module.new_name')])
    result = list(transformer._get_names_to_replace(mock_node))
    assert result == [('test_module.test_name', ('test_module.test_name', 'new_module.new_name'))]

def test_get_names_to_replace_no_rewrite(mock_node):
    transformer = MockBaseImportRewrite(rewrites=[])
    result = list(transformer._get_names_to_replace(mock_node))
    assert result == []

def test_get_names_to_replace_wildcard():
    node = ast.ImportFrom(
        module='test_module',
        names=[ast.alias(name='*', asname=None)],
        level=0
    )
    transformer = MockBaseImportRewrite(rewrites=[('test_module.test_name', 'new_module.new_name')])
    result = list(transformer._get_names_to_replace(node))
    assert result == []
