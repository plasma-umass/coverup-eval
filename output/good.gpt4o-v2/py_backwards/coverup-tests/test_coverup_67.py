# file: py_backwards/transformers/base.py:96-110
# asked: {"lines": [101, 102, 103], "branches": [[100, 101]]}
# gained: {"lines": [101, 102, 103], "branches": [[100, 101]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.base import BaseImportRewrite

def test_get_replaced_import_from_part_with_replacement():
    tree = ast.Module(body=[])
    transformer = BaseImportRewrite(tree)
    node = ast.ImportFrom(module='os', names=[ast.alias(name='path', asname=None)], level=0)
    alias = node.names[0]
    names_to_replace = {'os.path': ('os', 'sys')}
    
    result = transformer._get_replaced_import_from_part(node, alias, names_to_replace)
    
    assert isinstance(result, ast.ImportFrom)
    assert result.module == 'sys'
    assert result.names[0].name == 'path'
    assert result.level == 0

def test_get_replaced_import_from_part_without_replacement():
    tree = ast.Module(body=[])
    transformer = BaseImportRewrite(tree)
    node = ast.ImportFrom(module='os', names=[ast.alias(name='path', asname=None)], level=0)
    alias = node.names[0]
    names_to_replace = {}
    
    result = transformer._get_replaced_import_from_part(node, alias, names_to_replace)
    
    assert isinstance(result, ast.ImportFrom)
    assert result.module == 'os'
    assert result.names[0].name == 'path'
    assert result.level == 0
