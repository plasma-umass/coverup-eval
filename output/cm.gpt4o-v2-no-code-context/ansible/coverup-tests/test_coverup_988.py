# file: lib/ansible/playbook/play_context.py:339-355
# asked: {"lines": [343, 345, 346, 350, 353], "branches": [[342, 343], [345, 346], [345, 352], [349, 350], [352, 353]]}
# gained: {"lines": [343, 345, 346, 350, 353], "branches": [[342, 343], [345, 346], [345, 352], [349, 350], [352, 353]]}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the PlayContext class is imported from ansible.playbook.play_context
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def play_context():
    return PlayContext()

def test_connection_smart_with_controlpersist(play_context, monkeypatch):
    monkeypatch.setattr(play_context, '_attributes', {'connection': 'smart'})
    with patch('ansible.playbook.play_context.check_for_controlpersist', return_value=False):
        with patch('ansible.playbook.play_context.paramiko', new=MagicMock()):
            play_context._get_attr_connection()
            assert play_context.connection == 'paramiko'

def test_connection_smart_without_controlpersist(play_context, monkeypatch):
    monkeypatch.setattr(play_context, '_attributes', {'connection': 'smart'})
    with patch('ansible.playbook.play_context.check_for_controlpersist', return_value=True):
        play_context._get_attr_connection()
        assert play_context.connection == 'ssh'

def test_connection_persistent_with_paramiko(play_context, monkeypatch):
    monkeypatch.setattr(play_context, '_attributes', {'connection': 'persistent'})
    with patch('ansible.playbook.play_context.paramiko', new=MagicMock()):
        play_context._get_attr_connection()
        assert play_context.connection == 'paramiko'
