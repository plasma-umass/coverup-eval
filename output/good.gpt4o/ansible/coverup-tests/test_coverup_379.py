# file lib/ansible/cli/scripts/ansible_connection_cli_stub.py:73-86
# lines [73, 74, 75, 76, 77, 79, 80, 82, 83, 85, 86]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.cli.scripts.ansible_connection_cli_stub import ConnectionProcess

@pytest.fixture
def mock_json_rpc_server(mocker):
    return mocker.patch('ansible.cli.scripts.ansible_connection_cli_stub.JsonRpcServer')

def test_connection_process_initialization(mock_json_rpc_server):
    fd = Mock()
    play_context = Mock()
    socket_path = "/tmp/socket"
    original_path = "/tmp/original"
    task_uuid = "1234-5678"
    ansible_playbook_pid = 12345

    conn_process = ConnectionProcess(fd, play_context, socket_path, original_path, task_uuid, ansible_playbook_pid)

    assert conn_process.play_context == play_context
    assert conn_process.socket_path == socket_path
    assert conn_process.original_path == original_path
    assert conn_process._task_uuid == task_uuid
    assert conn_process.fd == fd
    assert conn_process.exception is None
    assert conn_process.srv == mock_json_rpc_server.return_value
    assert conn_process.sock is None
    assert conn_process.connection is None
    assert conn_process._ansible_playbook_pid == ansible_playbook_pid
