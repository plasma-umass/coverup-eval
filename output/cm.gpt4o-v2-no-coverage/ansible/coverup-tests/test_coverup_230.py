# file: lib/ansible/playbook/play.py:280-310
# asked: {"lines": [280, 290, 291, 292, 293, 294, 297, 298, 300, 302, 303, 304, 305, 306, 307, 308, 310], "branches": [[297, 298], [297, 300]]}
# gained: {"lines": [280, 290, 291, 292, 293, 294, 297, 298, 300, 302, 303, 304, 305, 306, 307, 308, 310], "branches": [[297, 298], [297, 300]]}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.play import Play
from ansible.playbook.block import Block

@pytest.fixture
def mock_play():
    play = Play()
    play._variable_manager = MagicMock()
    play._loader = MagicMock()
    play.pre_tasks = []
    play.tasks = []
    play.post_tasks = []
    play._compile_roles = MagicMock(return_value=[])
    return play

def test_compile_empty_tasks(mock_play):
    block_list = mock_play.compile()
    assert len(block_list) == 3
    assert all(isinstance(block, Block) for block in block_list)

def test_compile_with_pre_tasks(mock_play):
    mock_play.pre_tasks = [MagicMock()]
    block_list = mock_play.compile()
    assert len(block_list) == 4
    assert block_list[0] == mock_play.pre_tasks[0]

def test_compile_with_tasks(mock_play):
    mock_play.tasks = [MagicMock()]
    block_list = mock_play.compile()
    assert len(block_list) == 4
    assert block_list[1] == mock_play.tasks[0]

def test_compile_with_post_tasks(mock_play):
    mock_play.post_tasks = [MagicMock()]
    block_list = mock_play.compile()
    assert len(block_list) == 4
    assert block_list[2] == mock_play.post_tasks[0]

def test_compile_with_roles(mock_play):
    role_task = MagicMock()
    mock_play._compile_roles = MagicMock(return_value=[role_task])
    block_list = mock_play.compile()
    assert len(block_list) == 4
    assert block_list[1] == role_task
