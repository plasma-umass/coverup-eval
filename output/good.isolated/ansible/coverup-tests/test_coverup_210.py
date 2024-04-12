# file lib/ansible/playbook/play.py:350-365
# lines [350, 351, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 364, 365]
# branches ['356->exit', '356->357', '359->360', '359->364']

import pytest
from ansible.playbook.play import Play
from ansible.playbook.role import Role

# Mocking the Role class to avoid any side effects or dependencies
class MockRole(Role):
    def deserialize(self, data):
        pass

@pytest.fixture
def mock_role(mocker):
    mocker.patch('ansible.playbook.play.Role', new=MockRole)

def test_play_deserialize_includes_roles(mock_role):
    play = Play()

    # Mock data with 'roles' key to trigger the conditional branch
    mock_data = {
        'included_path': '/some/path',
        'action_groups': {'group1': 'action1'},
        'group_actions': {'action1': 'group1'},
        'roles': [{'name': 'role1'}, {'name': 'role2'}]
    }

    play.deserialize(mock_data)

    # Assertions to check if the roles have been deserialized and set correctly
    assert hasattr(play, 'roles'), "Play object should have 'roles' attribute after deserialization"
    assert isinstance(play.roles, list), "'roles' attribute should be a list"
    assert len(play.roles) == 2, "'roles' list should contain two elements"
    assert all(isinstance(role, MockRole) for role in play.roles), "All elements in 'roles' should be instances of MockRole"

    # Clean up by deleting the 'roles' attribute
    delattr(play, 'roles')
