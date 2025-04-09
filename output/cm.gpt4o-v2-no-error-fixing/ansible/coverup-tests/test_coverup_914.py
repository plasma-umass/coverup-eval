# file: lib/ansible/playbook/play.py:280-310
# asked: {"lines": [298], "branches": [[297, 298]]}
# gained: {"lines": [298], "branches": [[297, 298]]}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.play import Play
from ansible.playbook.block import Block

@pytest.fixture
def mock_block(mocker):
    mock_block = MagicMock(spec=Block)
    mock_block.block = [MagicMock()]
    mocker.patch('ansible.playbook.block.Block.load', return_value=mock_block)
    return mock_block

def test_compile_executes_all_lines(mock_block):
    play = Play()
    play._variable_manager = MagicMock()
    play._loader = MagicMock()
    play.pre_tasks = []
    play._compile_roles = MagicMock(return_value=[])
    play.tasks = []
    play.post_tasks = []

    block_list = play.compile()

    assert mock_block.block[0].implicit is True
    assert len(block_list) == 3
    assert block_list[0] == mock_block
    assert block_list[1] == mock_block
    assert block_list[2] == mock_block
