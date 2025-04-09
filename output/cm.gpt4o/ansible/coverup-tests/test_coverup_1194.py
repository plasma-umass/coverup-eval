# file lib/ansible/playbook/block.py:361-387
# lines [370, 371, 372]
# branches ['369->370', '371->368', '371->372']

import pytest
from unittest.mock import MagicMock
from ansible.playbook.block import Block

@pytest.fixture
def mock_play():
    play = MagicMock()
    play.only_tags = []
    play.skip_tags = []
    return play

def test_filter_tagged_tasks_with_nested_blocks(mock_play):
    # Create a nested block structure
    inner_block = Block()
    inner_block._play = mock_play
    inner_block.has_tasks = MagicMock(return_value=True)
    inner_block.copy = MagicMock(return_value=inner_block)
    inner_block.block = []
    inner_block.rescue = []
    inner_block.always = []

    outer_block = Block()
    outer_block._play = mock_play
    outer_block.has_tasks = MagicMock(return_value=True)
    outer_block.copy = MagicMock(return_value=outer_block)
    outer_block.block = [inner_block]
    outer_block.rescue = []
    outer_block.always = []

    # Execute the filter_tagged_tasks method
    filtered_block = outer_block.filter_tagged_tasks({})

    # Assertions to verify the postconditions
    assert filtered_block is not None
    assert isinstance(filtered_block, Block)
    assert len(filtered_block.block) == 1
    assert filtered_block.block[0] == inner_block

    # Clean up
    mock_play.reset_mock()
