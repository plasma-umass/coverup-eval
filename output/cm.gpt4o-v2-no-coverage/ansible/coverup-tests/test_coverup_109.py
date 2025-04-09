# file: lib/ansible/plugins/connection/paramiko_ssh.py:510-538
# asked: {"lines": [510, 516, 517, 519, 520, 522, 524, 526, 529, 530, 531, 533, 535, 536, 537, 538], "branches": [[516, 517], [516, 519], [524, 526], [524, 533], [526, 524], [526, 529], [530, 526], [530, 531], [533, 0], [533, 535], [535, 533], [535, 536], [537, 535], [537, 538]]}
# gained: {"lines": [510, 516, 517, 519, 520, 522, 524, 526, 529, 530, 531, 533, 535, 536, 537, 538], "branches": [[516, 517], [516, 519], [524, 526], [524, 533], [526, 524], [526, 529], [530, 526], [530, 531], [533, 0], [533, 535], [535, 533], [535, 536], [537, 535], [537, 538]]}

import os
import pytest
from unittest.mock import MagicMock, mock_open, patch
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.utils.path import makedirs_safe

@pytest.fixture
def connection(monkeypatch):
    play_context = MagicMock()
    new_stdin = MagicMock()
    shell = MagicMock()
    shell_loader = MagicMock()
    shell_loader.get = MagicMock(return_value=shell)
    monkeypatch.setattr('ansible.plugins.loader.shell_loader', shell_loader)
    conn = Connection(play_context, new_stdin)
    conn.ssh = MagicMock()
    return conn

def test_save_ssh_host_keys_no_keys_added(connection):
    connection._any_keys_added = MagicMock(return_value=False)
    result = connection._save_ssh_host_keys('dummy_filename')
    assert result is False

def test_save_ssh_host_keys_with_keys(connection, monkeypatch):
    connection._any_keys_added = MagicMock(return_value=True)
    connection.ssh._host_keys = {
        'hostname1': {
            'ssh-rsa': MagicMock(get_base64=MagicMock(return_value='base64key1')),
            'ssh-dss': MagicMock(get_base64=MagicMock(return_value='base64key2'))
        },
        'hostname2': {
            'ssh-rsa': MagicMock(get_base64=MagicMock(return_value='base64key3'))
        }
    }
    connection.ssh._host_keys['hostname1']['ssh-rsa']._added_by_ansible_this_time = False
    connection.ssh._host_keys['hostname1']['ssh-dss']._added_by_ansible_this_time = True
    connection.ssh._host_keys['hostname2']['ssh-rsa']._added_by_ansible_this_time = True

    mock_file = mock_open()
    monkeypatch.setattr('builtins.open', mock_file)
    monkeypatch.setattr('os.path.expanduser', lambda x: '/mocked/home/.ssh')
    monkeypatch.setattr('ansible.utils.path.makedirs_safe', MagicMock())

    connection._save_ssh_host_keys('dummy_filename')

    mock_file.assert_called_once_with('dummy_filename', 'w')
    handle = mock_file()
    handle.write.assert_any_call("hostname1 ssh-rsa base64key1\n")
    handle.write.assert_any_call("hostname1 ssh-dss base64key2\n")
    handle.write.assert_any_call("hostname2 ssh-rsa base64key3\n")
