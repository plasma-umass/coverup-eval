# file lib/ansible/playbook/block.py:361-387
# lines [361, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 379, 380, 381, 382, 383, 384, 385, 387]
# branches ['368->369', '368->377', '369->370', '369->373', '371->368', '371->372', '373->368', '373->376']

import pytest
from unittest.mock import MagicMock, create_autospec
from ansible.playbook.block import Block

@pytest.fixture
def mock_play():
    play = MagicMock()
    play.only_tags = set()
    play.skip_tags = set()
    return play

@pytest.fixture
def mock_task():
    task = MagicMock()
    task.action = 'some_action'
    task.implicit = False
    task.evaluate_tags = MagicMock(return_value=True)
    return task

@pytest.fixture
def mock_block(mock_play, mock_task):
    block = Block()
    block._play = mock_play
    block.block = [mock_task]
    block.rescue = []
    block.always = []
    block.has_tasks = MagicMock(return_value=True)
    block.copy = MagicMock(return_value=block)
    return block

def test_filter_tagged_tasks(mock_block, mock_task):
    all_vars = {}
    filtered_block = mock_block.filter_tagged_tasks(all_vars)
    
    # Assertions to verify the postconditions
    assert filtered_block is not None
    assert filtered_block.block == [mock_task]
    assert filtered_block.rescue == []
    assert filtered_block.always == []
    assert mock_task.evaluate_tags.called

    # Clean up
    mock_task.evaluate_tags.reset_mock()
    mock_block.copy.reset_mock()
    mock_block.has_tasks.reset_mock()
