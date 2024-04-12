# file lib/ansible/playbook/play.py:337-348
# lines [337, 338, 340, 341, 342, 343, 344, 345, 346, 348]
# branches ['341->342', '341->343']

import pytest
from ansible.playbook.play import Play
from ansible.playbook.role import Role

# Mock class for testing purposes
class MockRole(Role):
    def serialize(self):
        return {'mock_role': 'serialized'}

@pytest.fixture
def mock_play(mocker):
    play = Play()
    mocker.patch.object(play, 'get_roles', return_value=[MockRole()])
    play._included_path = '/fake/path'
    play._action_groups = ['group1', 'group2']
    play._group_actions = ['action1', 'action2']
    return play

def test_play_serialize(mock_play):
    serialized_data = mock_play.serialize()
    assert 'roles' in serialized_data
    assert serialized_data['roles'] == [{'mock_role': 'serialized'}]
    assert serialized_data['included_path'] == '/fake/path'
    assert serialized_data['action_groups'] == ['group1', 'group2']
    assert serialized_data['group_actions'] == ['action1', 'action2']
