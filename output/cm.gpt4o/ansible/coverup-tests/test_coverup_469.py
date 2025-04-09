# file lib/ansible/module_utils/connection.py:93-101
# lines [93, 94, 95, 96, 97, 98, 99, 100, 101]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.connection import exec_command, Connection, ConnectionError
from ansible.module_utils._text import to_text

@pytest.fixture
def mock_connection(mocker):
    mock_conn = mocker.patch('ansible.module_utils.connection.Connection')
    return mock_conn

def test_exec_command_success(mock_connection):
    module = Mock()
    module._socket_path = '/fake/path'
    command = 'fake_command'
    mock_connection.return_value.exec_command.return_value = 'command_output'

    code, out, err = exec_command(module, command)

    assert code == 0
    assert out == 'command_output'
    assert err == ''

def test_exec_command_connection_error(mock_connection):
    module = Mock()
    module._socket_path = '/fake/path'
    command = 'fake_command'
    mock_exception = ConnectionError('connection failed')
    mock_exception.code = 2
    mock_exception.err = 'connection failed'
    mock_connection.return_value.exec_command.side_effect = mock_exception

    code, out, err = exec_command(module, command)

    assert code == 2
    assert out == ''
    assert err == to_text('connection failed', errors='surrogate_then_replace')

def test_exec_command_connection_error_no_code(mock_connection):
    module = Mock()
    module._socket_path = '/fake/path'
    command = 'fake_command'
    mock_exception = ConnectionError('connection failed')
    mock_connection.return_value.exec_command.side_effect = mock_exception

    code, out, err = exec_command(module, command)

    assert code == 1
    assert out == ''
    assert err == to_text('connection failed', errors='surrogate_then_replace')
