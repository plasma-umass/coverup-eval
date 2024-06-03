# file lib/ansible/playbook/block.py:413-419
# lines [413, 414, 415, 416, 417, 418, 419]
# branches ['415->416', '415->419', '416->417', '416->418']

import pytest
from unittest.mock import Mock, patch

# Assuming the Block class and its dependencies are imported correctly
from ansible.playbook.block import Block
from ansible.playbook.task_include import TaskInclude

@pytest.fixture
def mock_parent():
    return Mock()

@pytest.fixture
def block_with_parent(mock_parent):
    block = Block()
    block._parent = mock_parent
    return block

def test_get_first_parent_include_direct_parent():
    block = Block()
    task_include = TaskInclude()
    block._parent = task_include

    result = block.get_first_parent_include()
    assert result == task_include

def test_get_first_parent_include_recursive_parent(mock_parent, block_with_parent):
    task_include = TaskInclude()
    mock_parent.get_first_parent_include.return_value = task_include

    result = block_with_parent.get_first_parent_include()
    assert result == task_include
    mock_parent.get_first_parent_include.assert_called_once()

def test_get_first_parent_include_no_parent():
    block = Block()
    block._parent = None

    result = block.get_first_parent_include()
    assert result is None
