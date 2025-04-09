# file: lib/ansible/playbook/play.py:312-313
# asked: {"lines": [313], "branches": []}
# gained: {"lines": [313], "branches": []}

import pytest
from ansible.playbook.play import Play
from ansible.utils.context_objects import CLIArgs

@pytest.fixture
def play_instance(monkeypatch):
    # Mocking context.CLIARGS to avoid dependency on actual CLI arguments
    monkeypatch.setattr("ansible.context.CLIARGS", CLIArgs({'tags': [], 'skip_tags': []}))
    return Play()

def test_play_init(play_instance):
    assert play_instance._included_conditional is None
    assert play_instance._included_path is None
    assert play_instance._removed_hosts == []
    assert play_instance.ROLE_CACHE == {}
    assert play_instance.only_tags == frozenset(('all',))
    assert play_instance.skip_tags == set()
    assert play_instance._action_groups == {}
    assert play_instance._group_actions == {}

def test_get_vars(play_instance, monkeypatch):
    # Mocking the vars attribute
    mock_vars = {'key': 'value'}
    monkeypatch.setattr(play_instance, 'vars', mock_vars)
    
    vars_copy = play_instance.get_vars()
    assert vars_copy == mock_vars
    assert vars_copy is not mock_vars  # Ensure it's a copy, not the same object
