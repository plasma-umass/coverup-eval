# file lib/ansible/playbook/play.py:350-365
# lines [351, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 364, 365]
# branches ['356->exit', '356->357', '359->360', '359->364']

import pytest
from ansible.playbook.play import Play
from ansible.playbook.role import Role

# Assuming that the Role class is defined in ansible.playbook.role
# and has a deserialize method that can be mocked.

@pytest.fixture
def mock_role(mocker):
    mock_role = mocker.MagicMock(spec=Role)
    mock_role.deserialize = mocker.MagicMock()
    return mock_role

def test_play_deserialize_with_roles(mock_role, mocker):
    mocker.patch('ansible.playbook.play.Role', return_value=mock_role)
    
    play = Play()
    data = {
        'included_path': '/some/path',
        'action_groups': {'group1': 'action1'},
        'group_actions': {'action1': 'group1'},
        'roles': [{'name': 'role1'}, {'name': 'role2'}]
    }
    
    play.deserialize(data)
    
    # Assertions to check if the roles have been deserialized and added to the play
    assert hasattr(play, 'roles')
    assert len(play.roles) == 2
    assert mock_role.deserialize.call_count == 2
    mock_role.deserialize.assert_any_call({'name': 'role1'})
    mock_role.deserialize.assert_any_call({'name': 'role2'})
    
    # Check if 'roles' key is deleted from data
    assert 'roles' not in data

    # Clean up
    del play
