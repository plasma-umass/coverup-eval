# file py_backwards/transformers/yield_from.py:55-65
# lines [55, 56, 57, 58, 59, 61, 62, 63, 64, 65]
# branches ['56->57', '58->59', '58->61']

import pytest
import ast
from py_backwards.transformers.yield_from import YieldFromTransformer
from py_backwards.transformers.base import BaseNodeTransformer

class MockNode:
    def __init__(self, body):
        self.body = body

class MockAssign:
    def __init__(self, targets, value):
        self.targets = targets
        self.value = value

@pytest.fixture
def transformer(mocker):
    mock_tree = mocker.Mock()
    return YieldFromTransformer(mock_tree)

def test_handle_assignments(transformer, mocker):
    # Mocking the methods used within _handle_assignments
    mocker.patch.object(transformer, '_get_yield_from_index', side_effect=[0, None])
    mocker.patch.object(transformer, '_emulate_yield_from', return_value=ast.Pass())
    mock_insert_at = mocker.patch('py_backwards.transformers.yield_from.insert_at')

    # Creating a mock node and assignment
    mock_node = MockNode(body=[MockAssign(targets=[ast.Name(id='x')], value=ast.Name(id='y'))])

    # Call the method
    result_node = transformer._handle_assignments(mock_node)

    # Assertions to verify the behavior
    assert result_node is mock_node
    assert transformer._tree_changed is True
    mock_insert_at.assert_called_once()

    # Clean up
    del transformer._tree_changed
