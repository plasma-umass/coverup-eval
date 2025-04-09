# file: lib/ansible/playbook/play.py:367-374
# asked: {"lines": [367, 368, 369, 370, 371, 372, 373, 374], "branches": []}
# gained: {"lines": [367, 368, 369, 370, 371, 372, 373, 374], "branches": []}

import pytest
from ansible.playbook.play import Play
from unittest.mock import MagicMock

@pytest.fixture
def play_instance():
    play = Play()
    play.ROLE_CACHE = {'role1': 'data1'}
    play._included_conditional = 'conditional'
    play._included_path = 'path'
    play._action_groups = 'action_groups'
    play._group_actions = 'group_actions'
    return play

def test_play_copy(play_instance):
    play_copy = play_instance.copy()

    assert play_copy is not play_instance
    assert play_copy.ROLE_CACHE == play_instance.ROLE_CACHE
    assert play_copy._included_conditional == play_instance._included_conditional
    assert play_copy._included_path == play_instance._included_path
    assert play_copy._action_groups == play_instance._action_groups
    assert play_copy._group_actions == play_instance._group_actions

    # Ensure that modifying the copy does not affect the original
    play_copy.ROLE_CACHE['role2'] = 'data2'
    assert 'role2' not in play_instance.ROLE_CACHE
