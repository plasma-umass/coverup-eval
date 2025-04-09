# file: py_backwards/utils/tree.py:48-55
# asked: {"lines": [48, 51, 52, 54, 55], "branches": [[51, 52], [51, 54], [54, 0], [54, 55]]}
# gained: {"lines": [48, 51, 52, 54, 55], "branches": [[51, 52], [51, 54], [54, 0], [54, 55]]}

import ast
import pytest

from py_backwards.utils.tree import insert_at

def test_insert_at_single_node():
    parent = ast.Module(body=[])
    node = ast.Expr(value=ast.Constant(value=42))
    insert_at(0, parent, node)
    assert len(parent.body) == 1
    assert isinstance(parent.body[0], ast.Expr)
    assert parent.body[0].value.value == 42

def test_insert_at_multiple_nodes():
    parent = ast.Module(body=[])
    nodes = [
        ast.Expr(value=ast.Constant(value=42)),
        ast.Expr(value=ast.Constant(value=43))
    ]
    insert_at(0, parent, nodes)
    assert len(parent.body) == 2
    assert isinstance(parent.body[0], ast.Expr)
    assert parent.body[0].value.value == 42
    assert isinstance(parent.body[1], ast.Expr)
    assert parent.body[1].value.value == 43

def test_insert_at_index():
    parent = ast.Module(body=[
        ast.Expr(value=ast.Constant(value=1)),
        ast.Expr(value=ast.Constant(value=2))
    ])
    node = ast.Expr(value=ast.Constant(value=42))
    insert_at(1, parent, node)
    assert len(parent.body) == 3
    assert isinstance(parent.body[1], ast.Expr)
    assert parent.body[1].value.value == 42

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # No specific cleanup needed for this test case
