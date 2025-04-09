# file: lib/ansible/cli/scripts/ansible_connection_cli_stub.py:73-86
# asked: {"lines": [73, 74, 75, 76, 77, 79, 80, 82, 83, 85, 86], "branches": []}
# gained: {"lines": [73, 74, 75, 76, 77, 79, 80, 82, 83, 85, 86], "branches": []}

import pytest
from ansible.cli.scripts.ansible_connection_cli_stub import ConnectionProcess

class MockJsonRpcServer:
    def __init__(self):
        pass

@pytest.fixture
def mock_json_rpc_server(monkeypatch):
    monkeypatch.setattr('ansible.cli.scripts.ansible_connection_cli_stub.JsonRpcServer', MockJsonRpcServer)

def test_connection_process_initialization(mock_json_rpc_server):
    fd = 1
    play_context = "play_context"
    socket_path = "/tmp/socket"
    original_path = "/tmp/original"
    task_uuid = "1234-5678"
    ansible_playbook_pid = 9999

    conn_process = ConnectionProcess(fd, play_context, socket_path, original_path, task_uuid, ansible_playbook_pid)

    assert conn_process.play_context == play_context
    assert conn_process.socket_path == socket_path
    assert conn_process.original_path == original_path
    assert conn_process._task_uuid == task_uuid
    assert conn_process.fd == fd
    assert conn_process.exception is None
    assert isinstance(conn_process.srv, MockJsonRpcServer)
    assert conn_process.sock is None
    assert conn_process.connection is None
    assert conn_process._ansible_playbook_pid == ansible_playbook_pid
