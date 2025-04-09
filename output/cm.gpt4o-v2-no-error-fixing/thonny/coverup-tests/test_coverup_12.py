# file: thonny/jedi_utils.py:20-43
# asked: {"lines": [20, 22, 24, 25, 26, 27, 28, 35, 37, 39, 40, 41, 42, 43], "branches": [[24, 25], [24, 43], [25, 24], [25, 26], [26, 37], [26, 39]]}
# gained: {"lines": [20, 22, 24, 25, 26, 27, 28, 35, 37, 39, 40, 43], "branches": [[24, 25], [24, 43], [25, 24], [25, 26], [26, 37], [26, 39]]}

import pytest
from parso.python import tree
from thonny.jedi_utils import _copy_of_get_statement_of_position

def test_copy_of_get_statement_of_position():
    # Create a mock node with children
    class MockNode:
        def __init__(self, children):
            self.children = children

    class MockChild:
        def __init__(self, start_pos, end_pos, type, is_flow=False, is_class_or_func=False):
            self.start_pos = start_pos
            self.end_pos = end_pos
            self.type = type
            self.is_flow = is_flow
            self.is_class_or_func = is_class_or_func

        def __getattr__(self, name):
            if name == 'children':
                return []
            raise AttributeError

    # Test case where child is directly returned
    child1 = MockChild((0, 0), (1, 1), 'expr_stmt')
    node = MockNode([child1])
    assert _copy_of_get_statement_of_position(node, (0, 0)) == child1

    # Test case where child is not directly returned and recursion happens
    child2 = MockChild((0, 0), (1, 1), 'suite')
    child3 = MockChild((0, 0), (1, 1), 'expr_stmt')
    child2.children = [child3]
    node = MockNode([child2])
    assert _copy_of_get_statement_of_position(node, (0, 0)) == child3

    # Test case where AttributeError is caught
    child4 = MockChild((0, 0), (1, 1), 'suite')
    node = MockNode([child4])
    assert _copy_of_get_statement_of_position(node, (0, 0)) is None

    # Test case where no child matches the position
    child5 = MockChild((2, 2), (3, 3), 'expr_stmt')
    node = MockNode([child5])
    assert _copy_of_get_statement_of_position(node, (0, 0)) is None
