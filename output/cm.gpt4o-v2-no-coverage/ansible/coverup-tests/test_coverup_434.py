# file: lib/ansible/playbook/play.py:328-335
# asked: {"lines": [328, 329, 330, 331, 332, 334, 335], "branches": [[330, 331], [330, 335], [331, 332], [331, 334]]}
# gained: {"lines": [328, 329, 330, 331, 332, 334, 335], "branches": [[330, 331], [330, 335], [331, 332], [331, 334]]}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.play import Play
from ansible.playbook.block import Block

@pytest.fixture
def mock_block():
    block = Block()
    block.block = ['block_task']
    block.rescue = ['rescue_task']
    block.always = ['always_task']
    return block

@pytest.fixture
def play_instance(mock_block):
    play = Play()
    play.pre_tasks = [mock_block]
    play.tasks = ['regular_task']
    play.post_tasks = []
    return play

def test_get_tasks_with_block(play_instance, mock_block):
    tasks = play_instance.get_tasks()
    assert tasks == [['block_task', 'rescue_task', 'always_task'], 'regular_task']

def test_get_tasks_without_block(monkeypatch):
    play = Play()
    play.pre_tasks = []
    play.tasks = ['regular_task']
    play.post_tasks = []

    tasks = play.get_tasks()
    assert tasks == ['regular_task']
