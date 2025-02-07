# file: lib/ansible/playbook/play.py:325-326
# asked: {"lines": [326], "branches": []}
# gained: {"lines": [326], "branches": []}

import pytest
from ansible.playbook.play import Play

@pytest.fixture
def play_instance():
    return Play()

def test_get_roles(play_instance):
    # Setup
    play_instance.roles = ['role1', 'role2', 'role3']
    
    # Execute
    roles = play_instance.get_roles()
    
    # Verify
    assert roles == ['role1', 'role2', 'role3']
    assert roles is not play_instance.roles  # Ensure a copy is returned

    # Cleanup
    play_instance.roles = []
