# file: py_backwards/transformers/starred_unpacking.py:20-25
# asked: {"lines": [20, 21, 22, 23, 25], "branches": [[21, 22], [21, 25], [22, 21], [22, 23]]}
# gained: {"lines": [20, 21, 22, 23, 25], "branches": [[21, 22], [21, 25], [22, 21], [22, 23]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.starred_unpacking import StarredUnpackingTransformer

def test_has_starred_with_starred():
    tree = ast.Module(body=[])
    transformer = StarredUnpackingTransformer(tree)
    nodes = [ast.Starred(value=ast.Name(id='a', ctx=ast.Load()), ctx=ast.Load())]
    assert transformer._has_starred(nodes) is True

def test_has_starred_without_starred():
    tree = ast.Module(body=[])
    transformer = StarredUnpackingTransformer(tree)
    nodes = [ast.Name(id='a', ctx=ast.Load())]
    assert transformer._has_starred(nodes) is False
