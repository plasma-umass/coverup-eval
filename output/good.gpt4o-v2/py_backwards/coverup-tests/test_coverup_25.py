# file: py_backwards/transformers/starred_unpacking.py:50-58
# asked: {"lines": [50, 52, 53, 55, 56, 57, 58], "branches": [[52, 53], [52, 55], [56, 57], [56, 58]]}
# gained: {"lines": [50, 52, 53, 55, 56, 57, 58], "branches": [[52, 53], [52, 55], [56, 57], [56, 58]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer

class ListEntry(ast.AST):
    pass

@pytest.fixture
def transformer():
    tree = ast.Module(body=[])
    return StarredUnpackingTransformer(tree)

def test_merge_lists_single_entry(transformer):
    entry = ListEntry()
    result = transformer._merge_lists([entry])
    assert result is entry

def test_merge_lists_two_entries(transformer):
    entry1 = ListEntry()
    entry2 = ListEntry()
    result = transformer._merge_lists([entry1, entry2])
    assert isinstance(result, ast.BinOp)
    assert result.left is entry1
    assert result.right is entry2
    assert isinstance(result.op, ast.Add)

def test_merge_lists_multiple_entries(transformer):
    entry1 = ListEntry()
    entry2 = ListEntry()
    entry3 = ListEntry()
    result = transformer._merge_lists([entry1, entry2, entry3])
    assert isinstance(result, ast.BinOp)
    assert isinstance(result.op, ast.Add)
    assert isinstance(result.left, ast.BinOp)
    assert result.left.left is entry1
    assert result.left.right is entry2
    assert result.right is entry3
