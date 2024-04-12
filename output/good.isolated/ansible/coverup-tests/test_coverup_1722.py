# file lib/ansible/playbook/play.py:325-326
# lines [326]
# branches []

import pytest
from ansible.playbook.play import Play

# Assuming that the Play class is part of a larger Ansible codebase and has dependencies
# that need to be mocked for isolated testing.

@pytest.fixture
def mock_play(mocker):
    # Mocking the Play class constructor to avoid side effects
    mocker.patch.object(Play, '__init__', return_value=None)
    play = Play()
    play.roles = ['role1', 'role2', 'role3']  # Setting up roles for the test
    return play

def test_get_roles(mock_play):
    # Test to ensure that get_roles method returns a copy of the roles list
    roles_copy = mock_play.get_roles()
    assert roles_copy == mock_play.roles  # Verify that the returned list matches the roles
    assert roles_copy is not mock_play.roles  # Verify that a copy is returned, not the original list

    # Modify the original list to ensure the returned list is indeed a copy
    mock_play.roles.append('role4')
    assert roles_copy != mock_play.roles  # The copy should not have the new role
