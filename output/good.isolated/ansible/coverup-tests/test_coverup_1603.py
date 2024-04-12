# file lib/ansible/plugins/connection/paramiko_ssh.py:484-499
# lines [487, 489, 491, 492, 493, 494, 496, 497, 498, 499]
# branches []

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.playbook.play_context import PlayContext
from unittest.mock import MagicMock, patch
from ansible.utils.display import Display

# Mock the Display class to prevent actual output during tests
display = Display()
display.vvv = MagicMock()

@pytest.fixture
def paramiko_connection(mocker):
    mocker.patch('ansible.plugins.connection.paramiko_ssh.Display', return_value=display)
    mocker.patch('ansible.plugins.connection.paramiko_ssh.super')
    mocker.patch('ansible.plugins.connection.paramiko_ssh.to_bytes', side_effect=lambda x, **kwargs: x)
    mocker.patch('ansible.plugins.connection.paramiko_ssh.to_native', side_effect=lambda x, **kwargs: x)
    
    play_context = PlayContext()
    play_context.remote_addr = 'testhost'
    
    connection = Connection(play_context, new_stdin=False)
    connection._connect_sftp = MagicMock()
    connection.sftp = MagicMock()
    
    return connection

def test_fetch_file_success(paramiko_connection):
    in_path = '/remote/path/to/file.txt'
    out_path = '/local/path/to/file.txt'
    
    paramiko_connection.fetch_file(in_path, out_path)
    
    paramiko_connection._connect_sftp.assert_called_once()
    paramiko_connection.sftp.get.assert_called_once_with(in_path, out_path)
    display.vvv.assert_called_once_with("FETCH %s TO %s" % (in_path, out_path), host=paramiko_connection._play_context.remote_addr)

def test_fetch_file_sftp_connection_failure(paramiko_connection):
    in_path = '/remote/path/to/file.txt'
    out_path = '/local/path/to/file.txt'
    
    paramiko_connection._connect_sftp.side_effect = Exception("SFTP connection failure")
    
    with pytest.raises(AnsibleError) as excinfo:
        paramiko_connection.fetch_file(in_path, out_path)
    
    assert "failed to open a SFTP connection" in str(excinfo.value)
    paramiko_connection._connect_sftp.assert_called_once()
    paramiko_connection.sftp.get.assert_not_called()

def test_fetch_file_ioerror(paramiko_connection):
    in_path = '/remote/path/to/file.txt'
    out_path = '/local/path/to/file.txt'
    
    paramiko_connection._connect_sftp.return_value = paramiko_connection.sftp
    paramiko_connection.sftp.get.side_effect = IOError("IO error during file transfer")
    
    with pytest.raises(AnsibleError) as excinfo:
        paramiko_connection.fetch_file(in_path, out_path)
    
    assert "failed to transfer file from" in str(excinfo.value)
    paramiko_connection._connect_sftp.assert_called_once()
    paramiko_connection.sftp.get.assert_called_once_with(in_path, out_path)
