# file lib/ansible/plugins/connection/paramiko_ssh.py:484-499
# lines [487, 489, 491, 492, 493, 494, 496, 497, 498, 499]
# branches []

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.playbook.play_context import PlayContext
from unittest.mock import MagicMock, patch
from ansible.module_utils._text import to_bytes

@pytest.fixture
def paramiko_connection(mocker):
    mocker.patch('ansible.plugins.connection.paramiko_ssh.super')
    connection = Connection(play_context=PlayContext(), new_stdin=None)
    connection._play_context.remote_addr = 'remote.test'
    connection._connect_sftp = MagicMock()
    return connection

def test_fetch_file_failure(paramiko_connection, mocker):
    # Mock display to avoid side effects
    mocker.patch('ansible.plugins.connection.paramiko_ssh.display')

    # Mock sftp connection to raise an exception on file transfer
    paramiko_connection._connect_sftp.return_value.get.side_effect = IOError

    # Define the in_path and out_path
    in_path = '/path/to/nonexistent/remote/file'
    out_path = '/path/to/local/destination'

    # Expect AnsibleError due to IOError during file transfer
    with pytest.raises(AnsibleError) as excinfo:
        paramiko_connection.fetch_file(in_path, out_path)

    # Check if the exception message matches the expected output
    assert "failed to transfer file from %s" % in_path in str(excinfo.value)

    # Verify that the SFTP connection was indeed called
    paramiko_connection._connect_sftp.assert_called_once()

    # Verify that the SFTP get method was called with the correct arguments
    paramiko_connection._connect_sftp.return_value.get.assert_called_once_with(
        to_bytes(in_path, errors='surrogate_or_strict'),
        to_bytes(out_path, errors='surrogate_or_strict')
    )
