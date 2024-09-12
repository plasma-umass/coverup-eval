# file: py_backwards/utils/tree.py:58-62
# asked: {"lines": [58, 61, 62], "branches": []}
# gained: {"lines": [58, 61, 62], "branches": []}

import ast
import pytest
from py_backwards.utils.tree import replace_at

def test_replace_at_with_single_node():
    class MockParent(ast.AST):
        def __init__(self):
            self.body = [ast.Pass(), ast.Break(), ast.Continue()]

    parent = MockParent()
    new_node = ast.Return(value=ast.Constant(value=42))
    replace_at(1, parent, new_node)
    
    assert len(parent.body) == 3
    assert isinstance(parent.body[1], ast.Return)
    assert parent.body[1].value.value == 42

def test_replace_at_with_multiple_nodes():
    class MockParent(ast.AST):
        def __init__(self):
            self.body = [ast.Pass(), ast.Break(), ast.Continue()]

    parent = MockParent()
    new_nodes = [ast.Return(value=ast.Constant(value=42)), ast.Expr(value=ast.Constant(value='test'))]
    replace_at(1, parent, new_nodes)
    
    assert len(parent.body) == 4
    assert isinstance(parent.body[1], ast.Return)
    assert parent.body[1].value.value == 42
    assert isinstance(parent.body[2], ast.Expr)
    assert parent.body[2].value.value == 'test'
