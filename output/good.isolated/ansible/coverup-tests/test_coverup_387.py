# file lib/ansible/cli/scripts/ansible_connection_cli_stub.py:73-86
# lines [73, 74, 75, 76, 77, 79, 80, 82, 83, 85, 86]
# branches []

import pytest
from ansible.cli.scripts.ansible_connection_cli_stub import ConnectionProcess
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def mock_play_context():
    return PlayContext()

@pytest.fixture
def mock_socket_path(tmp_path):
    return str(tmp_path / "socket")

@pytest.fixture
def mock_original_path(tmp_path):
    return str(tmp_path)

@pytest.fixture
def mock_fd(mocker):
    return mocker.MagicMock()

@pytest.fixture
def mock_task_uuid():
    return "123e4567-e89b-12d3-a456-426614174000"

@pytest.fixture
def mock_ansible_playbook_pid():
    return 1234

def test_connection_process_initialization(mock_fd, mock_play_context, mock_socket_path, mock_original_path, mock_task_uuid, mock_ansible_playbook_pid):
    connection_process = ConnectionProcess(
        fd=mock_fd,
        play_context=mock_play_context,
        socket_path=mock_socket_path,
        original_path=mock_original_path,
        task_uuid=mock_task_uuid,
        ansible_playbook_pid=mock_ansible_playbook_pid
    )

    assert connection_process.fd == mock_fd
    assert connection_process.play_context == mock_play_context
    assert connection_process.socket_path == mock_socket_path
    assert connection_process.original_path == mock_original_path
    assert connection_process._task_uuid == mock_task_uuid
    assert connection_process._ansible_playbook_pid == mock_ansible_playbook_pid
    assert connection_process.exception is None
    assert connection_process.srv is not None
    assert connection_process.sock is None
    assert connection_process.connection is None
