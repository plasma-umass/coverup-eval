# file: thonny/jedi_utils.py:20-43
# asked: {"lines": [22, 24, 25, 26, 27, 28, 35, 37, 39, 40, 41, 42, 43], "branches": [[24, 25], [24, 43], [25, 24], [25, 26], [26, 37], [26, 39]]}
# gained: {"lines": [22, 24, 25, 26, 27, 28, 35, 37, 39, 40, 43], "branches": [[24, 25], [24, 43], [25, 24], [25, 26], [26, 37], [26, 39]]}

import pytest
from parso.python import tree
from thonny.jedi_utils import _copy_of_get_statement_of_position

def test_get_statement_of_position_with_decorated_node(monkeypatch):
    class MockNode:
        def __init__(self, type, start_pos, end_pos, children=None):
            self.type = type
            self.start_pos = start_pos
            self.end_pos = end_pos
            self.children = children or []

    def mock_tree_flow():
        return tree.Flow

    def mock_tree_class_or_func():
        return tree.ClassOrFunc

    monkeypatch.setattr(tree, 'Flow', mock_tree_flow())
    monkeypatch.setattr(tree, 'ClassOrFunc', mock_tree_class_or_func())

    # Create a mock node structure
    leaf_node = MockNode(type="leaf", start_pos=(1, 0), end_pos=(1, 10))
    decorated_node = MockNode(type="decorated", start_pos=(0, 0), end_pos=(2, 0), children=[leaf_node])
    root_node = MockNode(type="root", start_pos=(0, 0), end_pos=(3, 0), children=[decorated_node])

    # Test position within the leaf node
    pos = (1, 5)
    result = _copy_of_get_statement_of_position(root_node, pos)
    assert result == leaf_node

def test_get_statement_of_position_with_non_scope_node(monkeypatch):
    class MockNode:
        def __init__(self, type, start_pos, end_pos, children=None):
            self.type = type
            self.start_pos = start_pos
            self.end_pos = end_pos
            self.children = children or []

    def mock_tree_flow():
        return tree.Flow

    def mock_tree_class_or_func():
        return tree.ClassOrFunc

    monkeypatch.setattr(tree, 'Flow', mock_tree_flow())
    monkeypatch.setattr(tree, 'ClassOrFunc', mock_tree_class_or_func())

    # Create a mock node structure
    non_scope_node = MockNode(type="non_scope", start_pos=(1, 0), end_pos=(1, 10))
    suite_node = MockNode(type="suite", start_pos=(0, 0), end_pos=(2, 0), children=[non_scope_node])
    root_node = MockNode(type="root", start_pos=(0, 0), end_pos=(3, 0), children=[suite_node])

    # Test position within the non-scope node
    pos = (1, 5)
    result = _copy_of_get_statement_of_position(root_node, pos)
    assert result == non_scope_node

def test_get_statement_of_position_with_no_matching_node(monkeypatch):
    class MockNode:
        def __init__(self, type, start_pos, end_pos, children=None):
            self.type = type
            self.start_pos = start_pos
            self.end_pos = end_pos
            self.children = children or []

    def mock_tree_flow():
        return tree.Flow

    def mock_tree_class_or_func():
        return tree.ClassOrFunc

    monkeypatch.setattr(tree, 'Flow', mock_tree_flow())
    monkeypatch.setattr(tree, 'ClassOrFunc', mock_tree_class_or_func())

    # Create a mock node structure
    leaf_node = MockNode(type="leaf", start_pos=(1, 0), end_pos=(1, 10))
    root_node = MockNode(type="root", start_pos=(0, 0), end_pos=(3, 0), children=[leaf_node])

    # Test position outside any node
    pos = (2, 5)
    result = _copy_of_get_statement_of_position(root_node, pos)
    assert result is None
