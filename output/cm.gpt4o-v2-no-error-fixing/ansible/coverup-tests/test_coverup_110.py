# file: lib/ansible/playbook/play.py:280-310
# asked: {"lines": [280, 290, 291, 292, 293, 294, 297, 298, 300, 302, 303, 304, 305, 306, 307, 308, 310], "branches": [[297, 298], [297, 300]]}
# gained: {"lines": [280, 290, 291, 292, 293, 294, 297, 300, 302, 303, 304, 305, 306, 307, 308, 310], "branches": [[297, 300]]}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.play import Play
from ansible.playbook.block import Block

@pytest.fixture
def play_instance():
    play = Play()
    play._variable_manager = MagicMock()
    play._loader = MagicMock()
    play.pre_tasks = [MagicMock()]
    play.tasks = [MagicMock()]
    play.post_tasks = [MagicMock()]
    play.roles = []
    return play

def test_compile(play_instance, mocker):
    mocker.patch.object(Block, 'load', return_value=Block())
    mocker.patch.object(Play, '_compile_roles', return_value=[MagicMock()])

    block_list = play_instance.compile()

    assert len(block_list) == 7
    assert isinstance(block_list[0], MagicMock)
    assert isinstance(block_list[1], Block)
    assert isinstance(block_list[2], MagicMock)
    assert isinstance(block_list[3], MagicMock)
    assert isinstance(block_list[4], Block)
    assert isinstance(block_list[5], MagicMock)
    assert isinstance(block_list[6], Block)
