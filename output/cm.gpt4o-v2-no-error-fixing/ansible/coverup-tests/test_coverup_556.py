# file: lib/ansible/playbook/play.py:101-102
# asked: {"lines": [101, 102], "branches": []}
# gained: {"lines": [101, 102], "branches": []}

import pytest
from ansible.playbook.play import Play

def test_play_repr(monkeypatch):
    # Create a mock for the get_name method
    def mock_get_name(self):
        return "mocked_name"
    
    # Apply the monkeypatch for Play.get_name
    monkeypatch.setattr(Play, "get_name", mock_get_name)
    
    # Instantiate Play and test __repr__
    play_instance = Play()
    assert repr(play_instance) == "mocked_name"
