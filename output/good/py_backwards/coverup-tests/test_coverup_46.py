# file py_backwards/transformers/base.py:96-110
# lines [99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
# branches ['100->101', '100->104']

import ast
import pytest
from unittest.mock import MagicMock
from py_backwards.transformers.base import BaseImportRewrite

class MockedBaseImportRewrite(BaseImportRewrite):
    def __init__(self):
        pass

@pytest.fixture
def base_import_rewrite():
    return MockedBaseImportRewrite()

@pytest.fixture
def import_from_node():
    return ast.ImportFrom(
        module='original_module',
        names=[ast.alias(name='original_name', asname=None)],
        level=0
    )

def test_get_replaced_import_from_part(base_import_rewrite, import_from_node):
    names_to_replace = {
        'original_module.original_name': ('original_module.original_name', 'new_module.new_name')
    }
    alias = ast.alias(name='original_name', asname=None)
    new_import_from = base_import_rewrite._get_replaced_import_from_part(import_from_node, alias, names_to_replace)
    
    assert new_import_from.module == 'new_module'
    assert len(new_import_from.names) == 1
    assert new_import_from.names[0].name == 'new_name'
    assert new_import_from.names[0].asname == 'original_name'
    assert new_import_from.level == 0
