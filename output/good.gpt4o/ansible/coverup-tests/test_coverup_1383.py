# file lib/ansible/cli/scripts/ansible_connection_cli_stub.py:88-123
# lines [89, 90, 91, 93, 98, 99, 100, 101, 102, 103, 104, 105, 106, 108, 109, 110, 112, 113, 114, 115, 116, 117, 118, 119, 121, 122, 123]
# branches ['98->99', '98->100']

import pytest
import os
import socket
import sys
import json
import traceback
from unittest import mock
from ansible.cli.scripts.ansible_connection_cli_stub import ConnectionProcess
from ansible.utils.unsafe_proxy import AnsibleUnsafeText
from ansible.module_utils._text import to_text
from ansible.parsing.ajson import AnsibleJSONEncoder

@pytest.fixture
def mock_play_context():
    return mock.Mock(
        private_key_file='test_key',
        connection='local'
    )

@pytest.fixture
def mock_srv():
    return mock.Mock()

@pytest.fixture
def mock_fd():
    return mock.Mock()

@pytest.fixture
def connection_process(mock_play_context, mock_srv, mock_fd):
    cp = ConnectionProcess(
        fd=mock_fd,
        play_context=mock_play_context,
        socket_path='/tmp/test_socket',
        original_path='/original/path'
    )
    cp.srv = mock_srv
    cp._task_uuid = 'test_uuid'
    cp._ansible_playbook_pid = 12345
    return cp

def test_connection_process_start(mocker, connection_process):
    mocker.patch('os.path.join', return_value='/original/path/test_key')
    mocker.patch('ansible.plugins.loader.connection_loader.get', return_value=mock.Mock())
    mock_stdout = mocker.patch('sys.stdout', new_callable=mock.Mock)
    mock_stdout.getvalue.return_value = 'test stdout message'
    mock_socket = mocker.patch('socket.socket')
    mock_socket_instance = mock_socket.return_value

    variables = {'test_var': 'value'}

    connection_process.start(variables)

    connection_process.play_context.private_key_file = '/original/path/test_key'
    connection_process.connection.set_options.assert_called_once_with(var_options=variables)
    connection_process.srv.register.assert_called_once_with(connection_process.connection)
    mock_socket_instance.bind.assert_called_once_with(connection_process.socket_path)
    mock_socket_instance.listen.assert_called_once_with(1)

    connection_process.fd.write.assert_called_once()
    result = json.loads(connection_process.fd.write.call_args[0][0])
    assert 'messages' in result
    assert any('control socket path is' in msg for level, msg in result['messages'])
    assert any('local domain socket listeners started successfully' in msg for level, msg in result['messages'])

    connection_process.fd.close.assert_called_once()
