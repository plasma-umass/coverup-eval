# file: lib/ansible/playbook/block.py:413-419
# asked: {"lines": [413, 414, 415, 416, 417, 418, 419], "branches": [[415, 416], [415, 419], [416, 417], [416, 418]]}
# gained: {"lines": [413, 414, 415, 416, 417, 418, 419], "branches": [[415, 416], [415, 419], [416, 417], [416, 418]]}

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.block import Block
from ansible.playbook.task_include import TaskInclude

@pytest.fixture
def mock_parent():
    return Mock(spec=Block)

def test_get_first_parent_include_with_task_include_parent(mock_parent):
    task_include = Mock(spec=TaskInclude)
    mock_parent._parent = task_include
    block = Block()
    block._parent = mock_parent._parent

    result = block.get_first_parent_include()

    assert result == task_include

def test_get_first_parent_include_with_non_task_include_parent(mock_parent):
    non_task_include_parent = Mock(spec=Block)
    non_task_include_parent.get_first_parent_include.return_value = 'non_task_include'
    mock_parent._parent = non_task_include_parent
    block = Block()
    block._parent = mock_parent._parent

    result = block.get_first_parent_include()

    assert result == 'non_task_include'
    non_task_include_parent.get_first_parent_include.assert_called_once()

def test_get_first_parent_include_with_no_parent():
    block = Block()
    block._parent = None

    result = block.get_first_parent_include()

    assert result is None
