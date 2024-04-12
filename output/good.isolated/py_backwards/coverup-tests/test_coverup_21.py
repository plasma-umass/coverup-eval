# file py_backwards/utils/tree.py:48-55
# lines [48, 51, 52, 54, 55]
# branches ['51->52', '51->54', '54->exit', '54->55']

import ast
import pytest
from py_backwards.utils.tree import insert_at

class DummyNode(ast.AST):
    _fields = ('body',)

@pytest.fixture
def dummy_node():
    node = DummyNode()
    node.body = []
    return node

def test_insert_at_single_node(dummy_node):
    new_node = ast.Pass()
    insert_at(0, dummy_node, new_node)
    assert len(dummy_node.body) == 1 and isinstance(dummy_node.body[0], ast.Pass), "The body should contain the new node"

def test_insert_at_multiple_nodes(dummy_node):
    new_nodes = [ast.Pass(), ast.Break()]
    insert_at(0, dummy_node, new_nodes)
    assert len(dummy_node.body) == 2 and isinstance(dummy_node.body[0], ast.Pass) and isinstance(dummy_node.body[1], ast.Break), "The body should contain the new nodes in order"

def test_insert_at_with_index(dummy_node):
    dummy_node.body = [ast.Pass()]
    new_node = ast.Break()
    insert_at(1, dummy_node, new_node)
    assert len(dummy_node.body) == 2 and isinstance(dummy_node.body[0], ast.Pass) and isinstance(dummy_node.body[1], ast.Break), "The body should contain the original and new node in order"

def test_insert_at_multiple_nodes_with_index(dummy_node):
    dummy_node.body = [ast.Pass()]
    new_nodes = [ast.Break(), ast.Continue()]
    insert_at(1, dummy_node, new_nodes)
    assert len(dummy_node.body) == 3 and isinstance(dummy_node.body[0], ast.Pass) and isinstance(dummy_node.body[1], ast.Break) and isinstance(dummy_node.body[2], ast.Continue), "The body should contain the original and new nodes in order"
