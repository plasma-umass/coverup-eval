# file lib/ansible/playbook/play.py:325-326
# lines [325, 326]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the Play class is imported from ansible.playbook.play
from ansible.playbook.play import Play

@pytest.fixture
def play_instance():
    # Create a mock instance of Play with roles attribute
    play = Play()
    play.roles = ['role1', 'role2', 'role3']
    yield play
    # Clean up if necessary

def test_get_roles(play_instance):
    roles = play_instance.get_roles()
    assert roles == ['role1', 'role2', 'role3']
    assert roles is not play_instance.roles  # Ensure a copy is returned
