# file: py_backwards/utils/tree.py:58-62
# asked: {"lines": [58, 61, 62], "branches": []}
# gained: {"lines": [58, 61, 62], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.tree import replace_at

def test_replace_at_with_single_node():
    class TestNode(ast.AST):
        _fields = ('body',)
        def __init__(self, body):
            self.body = body

    parent = TestNode(body=[ast.Pass(), ast.Break()])
    new_node = ast.Continue()

    replace_at(1, parent, new_node)

    assert len(parent.body) == 2
    assert isinstance(parent.body[1], ast.Continue)

def test_replace_at_with_multiple_nodes():
    class TestNode(ast.AST):
        _fields = ('body',)
        def __init__(self, body):
            self.body = body

    parent = TestNode(body=[ast.Pass(), ast.Break()])
    new_nodes = [ast.Continue(), ast.Return()]

    replace_at(1, parent, new_nodes)

    assert len(parent.body) == 3
    assert isinstance(parent.body[1], ast.Continue)
    assert isinstance(parent.body[2], ast.Return)
