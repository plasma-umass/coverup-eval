# file: lib/ansible/cli/scripts/ansible_connection_cli_stub.py:73-86
# asked: {"lines": [73, 74, 75, 76, 77, 79, 80, 82, 83, 85, 86], "branches": []}
# gained: {"lines": [73, 74, 75, 76, 77, 79, 80, 82, 83, 85, 86], "branches": []}

import pytest
from ansible.cli.scripts.ansible_connection_cli_stub import ConnectionProcess
from ansible.utils.jsonrpc import JsonRpcServer

class MockPlayContext:
    pass

@pytest.fixture
def connection_process():
    fd = 1
    play_context = MockPlayContext()
    socket_path = "/tmp/socket"
    original_path = "/tmp/original"
    task_uuid = "1234-5678"
    ansible_playbook_pid = 1000
    return ConnectionProcess(fd, play_context, socket_path, original_path, task_uuid, ansible_playbook_pid)

def test_connection_process_init(connection_process):
    assert connection_process.play_context is not None
    assert connection_process.socket_path == "/tmp/socket"
    assert connection_process.original_path == "/tmp/original"
    assert connection_process._task_uuid == "1234-5678"
    assert connection_process.fd == 1
    assert connection_process.exception is None
    assert isinstance(connection_process.srv, JsonRpcServer)
    assert connection_process.sock is None
    assert connection_process.connection is None
    assert connection_process._ansible_playbook_pid == 1000
