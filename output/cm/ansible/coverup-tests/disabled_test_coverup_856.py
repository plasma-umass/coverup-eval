# file lib/ansible/playbook/play.py:325-326
# lines [325, 326]
# branches []

import pytest
from ansible.playbook.play import Play

# Assuming the Play class is part of a larger module and has dependencies that need to be mocked
# We will use pytest-mock to mock those dependencies

@pytest.fixture
def mock_play(mocker):
    # Mocking the Base and CollectionSearch dependencies if necessary
    mocker.patch('ansible.playbook.play.Base')
    mocker.patch('ansible.playbook.play.CollectionSearch')
    # Create an instance of the Play class
    play = Play()
    # Set up the roles attribute with some test data
    play.roles = ['role1', 'role2', 'role3']
    return play

def test_get_roles(mock_play):
    # Call the get_roles method
    roles = mock_play.get_roles()
    # Assert that the returned list is a copy of the original roles list
    assert roles == ['role1', 'role2', 'role3']
    # Assert that modifying the returned list does not affect the original list
    roles.append('role4')
    assert mock_play.roles == ['role1', 'role2', 'role3']
