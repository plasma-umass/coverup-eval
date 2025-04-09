# file py_backwards/utils/tree.py:58-62
# lines [58, 61, 62]
# branches []

import ast
from py_backwards.utils.tree import replace_at
import pytest

class DummyNode(ast.AST):
    _fields = ('body',)

@pytest.fixture
def dummy_node():
    return DummyNode(body=[ast.Pass(), ast.Pass()])

def test_replace_at_single_node(dummy_node):
    new_node = ast.Break()
    replace_at(0, dummy_node, new_node)
    assert isinstance(dummy_node.body[0], ast.Break)
    assert len(dummy_node.body) == 2

def test_replace_at_multiple_nodes(dummy_node):
    new_nodes = [ast.Continue(), ast.Break()]
    replace_at(1, dummy_node, new_nodes)
    assert isinstance(dummy_node.body[1], ast.Continue)
    assert isinstance(dummy_node.body[2], ast.Break)
    assert len(dummy_node.body) == 3
