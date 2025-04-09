# file: py_backwards/utils/tree.py:58-62
# asked: {"lines": [58, 61, 62], "branches": []}
# gained: {"lines": [58, 61, 62], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.tree import replace_at

def test_replace_at_with_single_node():
    class MockParent(ast.AST):
        _fields = ['body']
        def __init__(self):
            self.body = [ast.Pass(), ast.Break()]

    parent = MockParent()
    new_node = ast.Continue()
    replace_at(0, parent, new_node)
    
    assert isinstance(parent.body[0], ast.Continue)
    assert isinstance(parent.body[1], ast.Break)

def test_replace_at_with_list_of_nodes():
    class MockParent(ast.AST):
        _fields = ['body']
        def __init__(self):
            self.body = [ast.Pass(), ast.Break()]

    parent = MockParent()
    new_nodes = [ast.Continue(), ast.Return()]
    replace_at(0, parent, new_nodes)
    
    assert isinstance(parent.body[0], ast.Continue)
    assert isinstance(parent.body[1], ast.Return)
    assert isinstance(parent.body[2], ast.Break)
