# file: py_backwards/utils/tree.py:41-45
# asked: {"lines": [41, 43, 44, 45], "branches": [[43, 0], [43, 44], [44, 43], [44, 45]]}
# gained: {"lines": [41, 43, 44, 45], "branches": [[43, 0], [43, 44], [44, 43], [44, 45]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.tree import find

def test_find_yields_correct_nodes():
    source_code = """
def foo():
    return 42
"""
    tree = ast.parse(source_code)
    nodes = list(find(tree, ast.FunctionDef))
    assert len(nodes) == 1
    assert isinstance(nodes[0], ast.FunctionDef)
    assert nodes[0].name == "foo"

def test_find_no_matching_nodes():
    source_code = """
x = 42
"""
    tree = ast.parse(source_code)
    nodes = list(find(tree, ast.FunctionDef))
    assert len(nodes) == 0

def test_find_multiple_matching_nodes():
    source_code = """
def foo():
    return 42

def bar():
    return 24
"""
    tree = ast.parse(source_code)
    nodes = list(find(tree, ast.FunctionDef))
    assert len(nodes) == 2
    assert nodes[0].name == "foo"
    assert nodes[1].name == "bar"
