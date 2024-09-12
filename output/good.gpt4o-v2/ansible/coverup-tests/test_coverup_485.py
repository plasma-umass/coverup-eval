# file: lib/ansible/playbook/play.py:367-374
# asked: {"lines": [367, 368, 369, 370, 371, 372, 373, 374], "branches": []}
# gained: {"lines": [367, 368, 369, 370, 371, 372, 373, 374], "branches": []}

import pytest
from ansible.playbook.play import Play

def test_play_copy():
    # Create an instance of Play
    original_play = Play()
    
    # Set attributes to non-default values
    original_play.ROLE_CACHE = {'role1': 'data1'}
    original_play._included_conditional = 'conditional'
    original_play._included_path = '/some/path'
    original_play._action_groups = {'group1': 'action1'}
    original_play._group_actions = {'action1': 'group1'}
    
    # Copy the play
    copied_play = original_play.copy()
    
    # Assertions to verify that the copy method works correctly
    assert copied_play is not original_play
    assert copied_play.ROLE_CACHE == original_play.ROLE_CACHE
    assert copied_play.ROLE_CACHE is not original_play.ROLE_CACHE
    assert copied_play._included_conditional == original_play._included_conditional
    assert copied_play._included_path == original_play._included_path
    assert copied_play._action_groups == original_play._action_groups
    assert copied_play._group_actions == original_play._group_actions
