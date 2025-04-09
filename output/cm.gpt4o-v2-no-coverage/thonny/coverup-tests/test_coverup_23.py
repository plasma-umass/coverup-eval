# file: thonny/jedi_utils.py:20-43
# asked: {"lines": [22, 24, 25, 26, 27, 28, 35, 37, 39, 40, 41, 42, 43], "branches": [[24, 25], [24, 43], [25, 24], [25, 26], [26, 37], [26, 39]]}
# gained: {"lines": [22, 24, 25, 26, 27, 28, 35, 37, 39, 40, 43], "branches": [[24, 25], [24, 43], [25, 26], [26, 37], [26, 39]]}

import pytest
from parso.python.tree import Node, Flow, ClassOrFunc
from thonny.jedi_utils import _copy_of_get_statement_of_position

class MockNode:
    def __init__(self, start_pos, end_pos, children=None, node_type=None):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.children = children or []
        self.type = node_type

def test_copy_of_get_statement_of_position_no_children():
    node = MockNode((0, 0), (10, 10))
    pos = (5, 5)
    assert _copy_of_get_statement_of_position(node, pos) is None

def test_copy_of_get_statement_of_position_with_matching_child():
    child = MockNode((0, 0), (10, 10), node_type="expr_stmt")
    node = MockNode((0, 0), (20, 20), children=[child])
    pos = (5, 5)
    assert _copy_of_get_statement_of_position(node, pos) == child

def test_copy_of_get_statement_of_position_with_non_matching_child():
    child = MockNode((0, 0), (10, 10), node_type="decorated")
    node = MockNode((0, 0), (20, 20), children=[child])
    pos = (5, 5)
    assert _copy_of_get_statement_of_position(node, pos) is None

def test_copy_of_get_statement_of_position_with_recursive_child():
    grandchild = MockNode((0, 0), (10, 10), node_type="expr_stmt")
    child = MockNode((0, 0), (20, 20), children=[grandchild], node_type="suite")
    node = MockNode((0, 0), (30, 30), children=[child])
    pos = (5, 5)
    assert _copy_of_get_statement_of_position(node, pos) == grandchild

def test_copy_of_get_statement_of_position_with_flow_child():
    child = MockNode((0, 0), (10, 10), node_type="expr_stmt")
    flow_child = MockNode((0, 0), (20, 20), children=[child], node_type="flow")
    node = MockNode((0, 0), (30, 30), children=[flow_child])
    pos = (5, 5)
    assert _copy_of_get_statement_of_position(node, pos) == flow_child

def test_copy_of_get_statement_of_position_with_classorfunc_child():
    child = MockNode((0, 0), (10, 10), node_type="expr_stmt")
    classorfunc_child = MockNode((0, 0), (20, 20), children=[child], node_type="classorfunc")
    node = MockNode((0, 0), (30, 30), children=[classorfunc_child])
    pos = (5, 5)
    assert _copy_of_get_statement_of_position(node, pos) == classorfunc_child
