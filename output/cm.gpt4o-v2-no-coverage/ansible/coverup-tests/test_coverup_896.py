# file: lib/ansible/playbook/play.py:325-326
# asked: {"lines": [325, 326], "branches": []}
# gained: {"lines": [325, 326], "branches": []}

import pytest
from ansible.playbook.play import Play

@pytest.fixture
def play_instance(monkeypatch):
    # Mocking context.CLIARGS to avoid dependency on actual CLI arguments
    monkeypatch.setattr('ansible.context.CLIARGS', {'tags': [], 'skip_tags': []})
    # Mocking the Base class __init__ method to avoid the TypeError
    monkeypatch.setattr('ansible.playbook.base.Base.__init__', lambda x: None)
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

def test_get_roles(play_instance, mocker):
    mock_roles = ['role1', 'role2']
    mocker.patch.object(play_instance, 'roles', mock_roles)
    assert play_instance.get_roles() == mock_roles
