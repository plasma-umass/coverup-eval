# file: lib/ansible/plugins/connection/paramiko_ssh.py:501-508
# asked: {"lines": [501, 503, 504, 505, 506, 507, 508], "branches": [[503, 504], [503, 508], [504, 503], [504, 505], [506, 504], [506, 507]]}
# gained: {"lines": [501, 503, 504, 505, 506, 507, 508], "branches": [[503, 504], [503, 508], [504, 503], [504, 505], [506, 504], [506, 507]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.connection.paramiko_ssh import Connection

@pytest.fixture
def connection():
    play_context = MagicMock()
    new_stdin = MagicMock()
    with patch('ansible.plugins.connection.get_shell_plugin', return_value=MagicMock()):
        conn = Connection(play_context, new_stdin)
    conn.ssh = MagicMock()
    return conn

def test_any_keys_added_true(connection):
    key_mock = MagicMock()
    key_mock._added_by_ansible_this_time = True
    connection.ssh._host_keys = {
        'hostname': {
            'keytype': key_mock
        }
    }
    assert connection._any_keys_added() is True

def test_any_keys_added_false(connection):
    key_mock = MagicMock()
    key_mock._added_by_ansible_this_time = False
    connection.ssh._host_keys = {
        'hostname': {
            'keytype': key_mock
        }
    }
    assert connection._any_keys_added() is False

def test_any_keys_added_empty(connection):
    connection.ssh._host_keys = {}
    assert connection._any_keys_added() is False
