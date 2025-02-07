# file: py_backwards/utils/tree.py:41-45
# asked: {"lines": [41, 43, 44, 45], "branches": [[43, 0], [43, 44], [44, 43], [44, 45]]}
# gained: {"lines": [41, 43, 44, 45], "branches": [[43, 0], [43, 44], [44, 43], [44, 45]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.tree import find

def test_find():
    # Create a simple AST tree
    tree = ast.parse("x = 1")

    # Test finding Assign nodes
    nodes = list(find(tree, ast.Assign))
    assert len(nodes) == 1
    assert isinstance(nodes[0], ast.Assign)

    # Test finding Name nodes
    nodes = list(find(tree, ast.Name))
    assert len(nodes) == 1
    assert isinstance(nodes[0], ast.Name)

    # Test finding nodes that do not exist in the tree
    nodes = list(find(tree, ast.FunctionDef))
    assert len(nodes) == 0
