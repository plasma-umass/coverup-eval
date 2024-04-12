# file lib/ansible/playbook/play.py:337-348
# lines [338, 340, 341, 342, 343, 344, 345, 346, 348]
# branches ['341->342', '341->343']

import pytest
from ansible.playbook.play import Play

# Assuming that the Play class has a constructor that can be called without arguments
# and that the get_roles method returns an empty list by default.
# Also assuming that the Play class has the _included_path, _action_groups, and _group_actions attributes.

class MockRole:
    def serialize(self):
        return {'mock_role': True}

@pytest.fixture
def mock_role(mocker):
    role = MockRole()
    mocker.patch.object(Play, 'get_roles', return_value=[role])
    return role

def test_play_serialize_includes_roles(mock_role):
    play = Play()
    serialized_data = play.serialize()

    assert 'roles' in serialized_data
    assert serialized_data['roles'] == [{'mock_role': True}]
    assert 'included_path' in serialized_data
    assert 'action_groups' in serialized_data
    assert 'group_actions' in serialized_data
