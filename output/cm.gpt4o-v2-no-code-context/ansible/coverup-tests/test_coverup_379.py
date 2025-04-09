# file: lib/ansible/plugins/connection/paramiko_ssh.py:484-499
# asked: {"lines": [484, 487, 489, 491, 492, 493, 494, 496, 497, 498, 499], "branches": []}
# gained: {"lines": [484, 487, 489, 491, 492, 493, 494, 496, 497, 498, 499], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.connection.paramiko_ssh import Connection, ConnectionBase
from ansible.errors import AnsibleError
from ansible.utils.display import Display
from ansible.playbook.play_context import PlayContext
from ansible.plugins.loader import shell_loader

@pytest.fixture
def connection():
    play_context = PlayContext()
    play_context.shell = 'sh'
    shell_plugin = shell_loader.get('sh')
    return Connection(play_context, None, shell=shell_plugin)

def test_fetch_file_success(monkeypatch, connection):
    in_path = "/remote/path"
    out_path = "/local/path"

    mock_sftp = MagicMock()
    mock_sftp.get = MagicMock()

    monkeypatch.setattr(connection, '_connect_sftp', lambda: mock_sftp)
    monkeypatch.setattr(Display, 'vvv', lambda *args, **kwargs: None)

    with patch.object(ConnectionBase, 'fetch_file', return_value=None):
        connection.fetch_file(in_path, out_path)

    mock_sftp.get.assert_called_once_with(in_path.encode('utf-8'), out_path.encode('utf-8'))

def test_fetch_file_sftp_connection_failure(monkeypatch, connection):
    in_path = "/remote/path"
    out_path = "/local/path"

    def mock_connect_sftp():
        raise Exception("SFTP connection error")

    monkeypatch.setattr(connection, '_connect_sftp', mock_connect_sftp)
    monkeypatch.setattr(Display, 'vvv', lambda *args, **kwargs: None)

    with patch.object(ConnectionBase, 'fetch_file', return_value=None):
        with pytest.raises(AnsibleError, match="failed to open a SFTP connection"):
            connection.fetch_file(in_path, out_path)

def test_fetch_file_transfer_failure(monkeypatch, connection):
    in_path = "/remote/path"
    out_path = "/local/path"

    mock_sftp = MagicMock()
    mock_sftp.get = MagicMock(side_effect=IOError("Transfer error"))

    monkeypatch.setattr(connection, '_connect_sftp', lambda: mock_sftp)
    monkeypatch.setattr(Display, 'vvv', lambda *args, **kwargs: None)

    with patch.object(ConnectionBase, 'fetch_file', return_value=None):
        with pytest.raises(AnsibleError, match="failed to transfer file from"):
            connection.fetch_file(in_path, out_path)
