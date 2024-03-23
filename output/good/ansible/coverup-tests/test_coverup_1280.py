# file lib/ansible/cli/scripts/ansible_connection_cli_stub.py:73-86
# lines [74, 75, 76, 77, 79, 80, 82, 83, 85, 86]
# branches []

import pytest
from ansible.cli.scripts.ansible_connection_cli_stub import ConnectionProcess
from unittest.mock import MagicMock

@pytest.fixture
def mock_json_rpc_server(mocker):
    return mocker.patch('ansible.cli.scripts.ansible_connection_cli_stub.JsonRpcServer', return_value=MagicMock())

def test_connection_process_initialization(mock_json_rpc_server):
    fd = 1
    play_context = 'play_context'
    socket_path = '/tmp/socket'
    original_path = '/original/path'
    task_uuid = '1234-5678'
    ansible_playbook_pid = 9999

    connection_process = ConnectionProcess(fd, play_context, socket_path, original_path, task_uuid, ansible_playbook_pid)

    assert connection_process.play_context == play_context
    assert connection_process.socket_path == socket_path
    assert connection_process.original_path == original_path
    assert connection_process._task_uuid == task_uuid
    assert connection_process.fd == fd
    assert connection_process.exception is None
    assert connection_process.sock is None
    assert connection_process.connection is None
    assert connection_process._ansible_playbook_pid == ansible_playbook_pid
    mock_json_rpc_server.assert_called_once()
