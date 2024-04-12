# file lib/ansible/playbook/play.py:367-374
# lines [367, 368, 369, 370, 371, 372, 373, 374]
# branches []

import pytest
from ansible.playbook.play import Play

# Assuming the existence of the Base and Taggable classes, and CollectionSearch module
# If they don't exist, they should be mocked or created for the purpose of this test

class Base:
    def copy(self):
        return Base()

class Taggable:
    pass

class CollectionSearch:
    pass

@pytest.fixture
def play_instance():
    play = Play()
    play.ROLE_CACHE = {'role1': 'cached_value'}
    play._included_conditional = 'some_conditional'
    play._included_path = 'some_path'
    play._action_groups = ['group1', 'group2']
    play._group_actions = {'group1': 'action1', 'group2': 'action2'}
    return play

def test_play_copy(play_instance):
    new_play = play_instance.copy()
    assert new_play.ROLE_CACHE == play_instance.ROLE_CACHE
    assert new_play._included_conditional == play_instance._included_conditional
    assert new_play._included_path == play_instance._included_path
    assert new_play._action_groups == play_instance._action_groups
    assert new_play._group_actions == play_instance._group_actions
    # Ensure that ROLE_CACHE is a copy, not the same reference
    assert new_play.ROLE_CACHE is not play_instance.ROLE_CACHE
    # Ensure that other attributes are the same reference (shallow copy)
    assert new_play._included_conditional is play_instance._included_conditional
    assert new_play._included_path is play_instance._included_path
    assert new_play._action_groups is play_instance._action_groups
    assert new_play._group_actions is play_instance._group_actions
