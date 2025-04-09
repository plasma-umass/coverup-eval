# file: py_backwards/utils/tree.py:9-12
# asked: {"lines": [9, 10, 11, 12], "branches": [[10, 0], [10, 11], [11, 10], [11, 12]]}
# gained: {"lines": [9, 10, 11, 12], "branches": [[10, 0], [10, 11], [11, 10], [11, 12]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.tree import _build_parents
from weakref import WeakKeyDictionary

def test_build_parents(monkeypatch):
    # Setup
    _parents = WeakKeyDictionary()
    monkeypatch.setattr('py_backwards.utils.tree._parents', _parents)

    # Create a simple AST
    tree = ast.parse("a = 1")

    # Call the function
    _build_parents(tree)

    # Assertions
    assert len(_parents) > 0
    for child, parent in _parents.items():
        assert isinstance(child, ast.AST)
        assert isinstance(parent, ast.AST)

    # Cleanup
    _parents.clear()
