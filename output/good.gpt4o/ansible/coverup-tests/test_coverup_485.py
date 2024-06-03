# file lib/ansible/playbook/play.py:367-374
# lines [367, 368, 369, 370, 371, 372, 373, 374]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the Play class is imported from ansible.playbook.play
from ansible.playbook.play import Play

class TestPlay:
    def test_copy_method(self, mocker):
        # Create a mock instance of Play
        play_instance = Play()
        
        # Mock the attributes that are copied
        play_instance.ROLE_CACHE = {'role1': 'data1'}
        play_instance._included_conditional = 'conditional'
        play_instance._included_path = 'path'
        play_instance._action_groups = 'action_groups'
        play_instance._group_actions = 'group_actions'
        
        # Mock the copy method of the superclass
        mock_super_copy = mocker.patch('ansible.playbook.play.Base.copy', return_value=MagicMock(spec=Play))
        
        # Call the copy method
        new_play_instance = play_instance.copy()
        
        # Assertions to verify the copied attributes
        assert new_play_instance.ROLE_CACHE == play_instance.ROLE_CACHE
        assert new_play_instance._included_conditional == play_instance._included_conditional
        assert new_play_instance._included_path == play_instance._included_path
        assert new_play_instance._action_groups == play_instance._action_groups
        assert new_play_instance._group_actions == play_instance._group_actions
        
        # Verify that the superclass copy method was called
        mock_super_copy.assert_called_once_with()
