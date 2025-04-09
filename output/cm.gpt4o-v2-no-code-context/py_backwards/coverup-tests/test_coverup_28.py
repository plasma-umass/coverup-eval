# file: py_backwards/utils/tree.py:58-62
# asked: {"lines": [58, 61, 62], "branches": []}
# gained: {"lines": [58, 61, 62], "branches": []}

import ast
import pytest
from py_backwards.utils.tree import replace_at, insert_at

@pytest.fixture
def mock_insert_at(mocker):
    return mocker.patch('py_backwards.utils.tree.insert_at')

def test_replace_at_with_single_node(mock_insert_at):
    class MockParent:
        def __init__(self):
            self.body = [ast.Pass(), ast.Pass(), ast.Pass()]

    parent = MockParent()
    new_node = ast.Break()
    replace_at(1, parent, new_node)
    
    assert len(parent.body) == 2
    assert isinstance(parent.body[0], ast.Pass)
    assert isinstance(parent.body[1], ast.Pass)
    mock_insert_at.assert_called_once_with(1, parent, new_node)

def test_replace_at_with_list_of_nodes(mock_insert_at):
    class MockParent:
        def __init__(self):
            self.body = [ast.Pass(), ast.Pass(), ast.Pass()]

    parent = MockParent()
    new_nodes = [ast.Break(), ast.Continue()]
    replace_at(1, parent, new_nodes)
    
    assert len(parent.body) == 2
    assert isinstance(parent.body[0], ast.Pass)
    assert isinstance(parent.body[1], ast.Pass)
    mock_insert_at.assert_called_once_with(1, parent, new_nodes)
