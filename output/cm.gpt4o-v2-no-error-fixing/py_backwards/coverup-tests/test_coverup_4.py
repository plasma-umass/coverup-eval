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

class Bar:
    def baz(self):
        return 'hello'
"""
    tree = ast.parse(source_code)
    
    # Test finding all function definitions
    func_defs = list(find(tree, ast.FunctionDef))
    assert len(func_defs) == 2
    assert func_defs[0].name == 'foo'
    assert func_defs[1].name == 'baz'
    
    # Test finding all class definitions
    class_defs = list(find(tree, ast.ClassDef))
    assert len(class_defs) == 1
    assert class_defs[0].name == 'Bar'

def test_find_no_matching_nodes():
    source_code = """
def foo():
    return 42
"""
    tree = ast.parse(source_code)
    
    # Test finding all class definitions in a tree with no classes
    class_defs = list(find(tree, ast.ClassDef))
    assert len(class_defs) == 0

@pytest.fixture
def clean_ast_tree():
    source_code = ""
    return ast.parse(source_code)

def test_find_with_empty_tree(clean_ast_tree):
    tree = clean_ast_tree
    
    # Test finding all function definitions in an empty tree
    func_defs = list(find(tree, ast.FunctionDef))
    assert len(func_defs) == 0
    
    # Test finding all class definitions in an empty tree
    class_defs = list(find(tree, ast.ClassDef))
    assert len(class_defs) == 0
