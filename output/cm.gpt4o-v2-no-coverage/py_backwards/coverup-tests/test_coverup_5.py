# file: py_backwards/transformers/starred_unpacking.py:20-25
# asked: {"lines": [20, 21, 22, 23, 25], "branches": [[21, 22], [21, 25], [22, 21], [22, 23]]}
# gained: {"lines": [20, 21, 22, 23, 25], "branches": [[21, 22], [21, 25], [22, 21], [22, 23]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer

@pytest.fixture
def transformer():
    return StarredUnpackingTransformer(None)

def test_has_starred_with_starred(transformer):
    starred_node = ast.Starred(value=ast.Name(id='x', ctx=ast.Load()), ctx=ast.Load())
    assert transformer._has_starred([starred_node]) is True

def test_has_starred_without_starred(transformer):
    name_node = ast.Name(id='x', ctx=ast.Load())
    assert transformer._has_starred([name_node]) is False

def test_has_starred_empty_list(transformer):
    assert transformer._has_starred([]) is False
