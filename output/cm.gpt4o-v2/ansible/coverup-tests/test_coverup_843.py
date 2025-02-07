# file: lib/ansible/playbook/play.py:101-102
# asked: {"lines": [101, 102], "branches": []}
# gained: {"lines": [101, 102], "branches": []}

import pytest
from ansible.playbook.play import Play

class MockBase:
    def get_name(self):
        return "mock_name"

@pytest.fixture
def mock_play(monkeypatch):
    monkeypatch.setattr(Play, "get_name", MockBase().get_name)
    return Play()

def test_play_repr(mock_play):
    assert repr(mock_play) == "mock_name"
