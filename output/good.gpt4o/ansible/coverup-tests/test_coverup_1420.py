# file lib/ansible/playbook/block.py:179-222
# lines [191, 192, 193, 195]
# branches ['186->191', '192->193', '192->195']

import pytest
from unittest.mock import Mock
from ansible.playbook.block import Block

@pytest.fixture
def mock_task():
    task = Mock()
    task.copy.return_value = task
    task._parent = None
    return task

@pytest.fixture
def mock_block(mock_task):
    block = Block()
    block.block = [mock_task]
    block.rescue = []
    block.always = []
    block._parent = None
    block._play = None
    block._use_handlers = None
    block._dep_chain = None
    block._role = None
    return block

def test_copy_with_nested_parent(mock_block, mock_task):
    # Setup a nested parent structure
    parent_task = Mock()
    parent_task.copy.return_value = parent_task
    parent_task._parent = mock_block

    mock_task._parent = parent_task

    # Perform the copy
    new_block = mock_block.copy()

    # Assertions to verify the correct parent structure
    assert new_block.block[0]._parent == parent_task
    assert new_block.block[0]._parent._parent == new_block

    # Clean up
    mock_task._parent = None
    parent_task._parent = None
