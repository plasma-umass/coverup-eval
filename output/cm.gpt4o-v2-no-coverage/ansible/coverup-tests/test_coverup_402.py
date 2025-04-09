# file: lib/ansible/playbook/play.py:337-348
# asked: {"lines": [337, 338, 340, 341, 342, 343, 344, 345, 346, 348], "branches": [[341, 342], [341, 343]]}
# gained: {"lines": [337, 338, 340, 341, 342, 343, 344, 345, 346, 348], "branches": [[341, 342], [341, 343]]}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.play import Play

@pytest.fixture
def play_instance(monkeypatch):
    play = Play()
    play.roles = [MagicMock(), MagicMock()]
    play._included_path = "some_path"
    play._action_groups = ["group1", "group2"]
    play._group_actions = ["action1", "action2"]
    
    for role in play.roles:
        role.serialize = MagicMock(return_value={"role": "data"})
    
    return play

def test_serialize(play_instance):
    serialized_data = play_instance.serialize()
    
    assert 'roles' in serialized_data
    assert len(serialized_data['roles']) == 2
    assert serialized_data['roles'][0] == {"role": "data"}
    assert serialized_data['roles'][1] == {"role": "data"}
    assert serialized_data['included_path'] == "some_path"
    assert serialized_data['action_groups'] == ["group1", "group2"]
    assert serialized_data['group_actions'] == ["action1", "action2"]
