# file lib/ansible/playbook/play.py:280-310
# lines [280, 290, 291, 292, 293, 294, 297, 298, 300, 302, 303, 304, 305, 306, 307, 308, 310]
# branches ['297->298', '297->300']

import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.play import Play
from ansible.playbook.block import Block

@pytest.fixture
def mock_block(mocker):
    mock_block = mocker.patch('ansible.playbook.block.Block.load')
    mock_block.return_value = MagicMock(block=[MagicMock()])
    return mock_block

@pytest.fixture
def play_instance(mocker, mock_block):
    mocker.patch('ansible.playbook.play.Play._compile_roles', return_value=[])
    play = Play()
    play.pre_tasks = []
    play.tasks = []
    play.post_tasks = []
    play._variable_manager = MagicMock()
    play._loader = MagicMock()
    return play

def test_compile(play_instance, mock_block):
    block_list = play_instance.compile()
    
    # Assertions to verify the block list contains the expected flush handlers and tasks
    assert len(block_list) == 3  # pre_tasks, flush_block, flush_block, flush_block
    assert block_list[0] == mock_block.return_value
    assert block_list[1] == mock_block.return_value
    assert block_list[2] == mock_block.return_value
    
    # Verify that the flush handlers meta task is marked as implicit
    for task in mock_block.return_value.block:
        assert task.implicit is True
