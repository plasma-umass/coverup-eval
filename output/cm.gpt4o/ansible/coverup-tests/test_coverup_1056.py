# file lib/ansible/playbook/block.py:179-222
# lines [181, 182, 183, 184, 185, 186, 188, 191, 192, 193, 195, 197, 198, 199, 206, 210, 213, 214, 215, 219]
# branches ['182->183', '182->199', '184->185', '184->197', '186->188', '186->191', '192->193', '192->195', '205->206', '209->210', '212->213', '218->219']

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
    block._play = Mock()
    block._use_handlers = Mock()
    block._dep_chain = [Mock()]
    block._parent = Mock()
    block._parent.copy.return_value = block._parent
    block.block = [mock_task]
    block.rescue = [mock_task]
    block.always = [mock_task]
    block._role = Mock()
    return block

def test_block_copy(mock_block, mock_task):
    new_block = mock_block.copy()

    # Assertions to verify the postconditions
    assert new_block._play == mock_block._play
    assert new_block._use_handlers == mock_block._use_handlers
    assert new_block._dep_chain == mock_block._dep_chain
    assert new_block._parent == mock_block._parent
    assert new_block.block == mock_block.block
    assert new_block.rescue == mock_block.rescue
    assert new_block.always == mock_block.always
    assert new_block._role == mock_block._role

    # Ensure the tasks were copied correctly
    for task in new_block.block + new_block.rescue + new_block.always:
        assert task.copy.called
        assert task._parent == new_block

    # Clean up
    mock_block._play = None
    mock_block._use_handlers = None
    mock_block._dep_chain = None
    mock_block._parent = None
    mock_block.block = None
    mock_block.rescue = None
    mock_block.always = None
    mock_block._role = None
