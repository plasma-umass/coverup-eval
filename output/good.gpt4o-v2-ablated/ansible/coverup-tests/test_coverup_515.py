# file: lib/ansible/playbook/play.py:325-326
# asked: {"lines": [326], "branches": []}
# gained: {"lines": [326], "branches": []}

import pytest
from unittest.mock import MagicMock

# Assuming the Play class is defined in ansible.playbook.play module
from ansible.playbook.play import Play

class TestPlay:
    @pytest.fixture
    def play_instance(self):
        # Create a Play instance with mock roles
        play = Play()
        play.roles = ['role1', 'role2', 'role3']
        return play

    def test_get_roles(self, play_instance):
        roles = play_instance.get_roles()
        assert roles == ['role1', 'role2', 'role3']
        assert roles is not play_instance.roles  # Ensure a copy is returned

    def test_get_roles_empty(self, monkeypatch):
        play = Play()
        monkeypatch.setattr(play, 'roles', [])
        roles = play.get_roles()
        assert roles == []
        assert roles is not play.roles  # Ensure a copy is returned
