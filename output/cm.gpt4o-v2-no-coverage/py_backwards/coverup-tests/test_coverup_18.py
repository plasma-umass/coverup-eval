# file: py_backwards/transformers/base.py:87-94
# asked: {"lines": [87, 89, 90, 91, 92, 93, 94], "branches": [[89, 0], [89, 90], [91, 89], [91, 92], [93, 89], [93, 94]]}
# gained: {"lines": [87, 89, 90, 91, 92, 93, 94], "branches": [[89, 0], [89, 90], [91, 89], [91, 92], [93, 89], [93, 94]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.base import BaseImportRewrite

class MockBaseImportRewrite(BaseImportRewrite):
    def __init__(self, rewrites):
        self.rewrites = rewrites

@pytest.fixture
def mock_rewrite():
    return MockBaseImportRewrite(rewrites=[('module.old', 'module.new')])

def test_get_names_to_replace_with_rewrite(mock_rewrite):
    node = ast.ImportFrom(module='module', names=[ast.alias(name='old', asname=None)], level=0)
    result = list(mock_rewrite._get_names_to_replace(node))
    assert result == [('module.old', ('module.old', 'module.new'))]

def test_get_names_to_replace_without_rewrite(mock_rewrite):
    node = ast.ImportFrom(module='module', names=[ast.alias(name='new', asname=None)], level=0)
    result = list(mock_rewrite._get_names_to_replace(node))
    assert result == []

def test_get_names_to_replace_with_wildcard(mock_rewrite):
    node = ast.ImportFrom(module='module', names=[ast.alias(name='*', asname=None)], level=0)
    result = list(mock_rewrite._get_names_to_replace(node))
    assert result == []

def test_get_matched_rewrite_exact_match(mock_rewrite):
    result = mock_rewrite._get_matched_rewrite('module.old')
    assert result == ('module.old', 'module.new')

def test_get_matched_rewrite_prefix_match(mock_rewrite):
    result = mock_rewrite._get_matched_rewrite('module.old.submodule')
    assert result == ('module.old', 'module.new')

def test_get_matched_rewrite_no_match(mock_rewrite):
    result = mock_rewrite._get_matched_rewrite('module.other')
    assert result is None

def test_get_matched_rewrite_none():
    mock_rewrite = MockBaseImportRewrite(rewrites=[])
    result = mock_rewrite._get_matched_rewrite(None)
    assert result is None
