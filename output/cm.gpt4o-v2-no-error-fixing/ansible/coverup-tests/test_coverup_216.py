# file: lib/ansible/playbook/play.py:337-348
# asked: {"lines": [337, 338, 340, 341, 342, 343, 344, 345, 346, 348], "branches": [[341, 342], [341, 343]]}
# gained: {"lines": [337, 338, 340, 341, 342, 343, 344, 345, 346, 348], "branches": [[341, 342], [341, 343]]}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.play import Play

@pytest.fixture
def play_instance():
    play = Play()
    play._included_path = "some_path"
    play._action_groups = {"group1": "action1"}
    play._group_actions = {"action1": "group1"}
    return play

def test_serialize(play_instance, mocker):
    mocker.patch.object(Play, 'get_roles', return_value=[MagicMock(serialize=lambda: "role1")])
    serialized_data = play_instance.serialize()
    
    assert 'roles' in serialized_data
    assert serialized_data['roles'] == ["role1"]
    assert serialized_data['included_path'] == "some_path"
    assert serialized_data['action_groups'] == {"group1": "action1"}
    assert serialized_data['group_actions'] == {"action1": "group1"}
