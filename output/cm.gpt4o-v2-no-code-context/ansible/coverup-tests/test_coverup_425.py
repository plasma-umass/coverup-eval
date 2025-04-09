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
    original_play = play_instance

    # Mock the super().copy() method
    with pytest.MonkeyPatch.context() as mp:
        mock_copy = MagicMock(return_value=Play())
        mp.setattr('ansible.playbook.play.Base.copy', mock_copy)

        copied_play = original_play.copy()

        # Assertions to verify the copied attributes
        assert copied_play.ROLE_CACHE == original_play.ROLE_CACHE
        assert copied_play._included_conditional == original_play._included_conditional
        assert copied_play._included_path == original_play._included_path
        assert copied_play._action_groups == original_play._action_groups
        assert copied_play._group_actions == original_play._group_actions

        # Ensure the mock copy method was called
        mock_copy.assert_called_once()
