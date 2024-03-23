# file lib/ansible/playbook/play.py:325-326
# lines [326]
# branches []

import pytest
from ansible.playbook.play import Play

# Assuming the Play class is part of a larger module and has dependencies that need to be mocked
# We will use pytest-mock to mock those dependencies if necessary

def test_get_roles(mocker):
    # Setup: Create a mock Play object with a roles attribute
    mock_play = Play()
    mock_play.roles = ['role1', 'role2', 'role3']

    # Exercise: Call the get_roles method
    result = mock_play.get_roles()

    # Verify: Check that the result is a copy of the roles list
    assert result == ['role1', 'role2', 'role3']
    assert result is not mock_play.roles  # Ensure a copy was returned, not the original list

    # Cleanup: Nothing to clean up in this test
