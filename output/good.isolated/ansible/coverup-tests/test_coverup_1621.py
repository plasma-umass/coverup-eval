# file lib/ansible/playbook/play.py:367-374
# lines [368, 369, 370, 371, 372, 373, 374]
# branches []

import pytest
from ansible.playbook.play import Play

# Assuming that Base, Taggable, CollectionSearch are properly defined somewhere in the ansible codebase
# and that ROLE_CACHE, _included_conditional, _included_path, _action_groups, and _group_actions are attributes of Play

class TestPlayCopy:

    def test_play_copy(self, mocker):
        # Create a Play object with necessary attributes
        play = Play()
        play.ROLE_CACHE = {'role1': 'cache1'}
        play._included_conditional = 'conditional'
        play._included_path = 'path'
        play._action_groups = ['group1', 'group2']
        play._group_actions = {'group1': 'action1'}

        # Call the copy method
        new_play = play.copy()

        # Assertions to check if the copy was correct
        assert new_play.ROLE_CACHE == play.ROLE_CACHE
        assert new_play._included_conditional == play._included_conditional
        assert new_play._included_path == play._included_path
        assert new_play._action_groups == play._action_groups
        assert new_play._group_actions == play._group_actions

        # Ensure that the ROLE_CACHE is a copy, not the same object
        assert new_play.ROLE_CACHE is not play.ROLE_CACHE
        assert new_play.ROLE_CACHE == {'role1': 'cache1'}

        # Clean up is not necessary as we are not affecting any global state
