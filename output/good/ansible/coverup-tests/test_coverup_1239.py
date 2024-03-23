# file lib/ansible/executor/process/worker.py:63-78
# lines [64, 65, 66, 67, 68, 69, 72, 73, 75, 77, 78]
# branches ['66->67', '66->77', '77->exit', '77->78']

import os
import sys
import pytest
from unittest.mock import MagicMock, Mock
from ansible.executor.process.worker import WorkerProcess

@pytest.fixture
def mock_stdin(mocker):
    mock_stdin = mocker.patch('sys.stdin', spec=True)
    return mock_stdin

@pytest.fixture
def worker_process(mocker):
    final_q = Mock()
    task_vars = {}
    host = Mock()
    task = Mock()
    play_context = Mock()
    loader = Mock()
    variable_manager = Mock()
    shared_loader_obj = Mock()
    worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    return worker

def test_worker_process_save_stdin_tty_with_valid_fileno(mock_stdin, worker_process, mocker):
    # Setup the mock for sys.stdin to simulate isatty() and fileno()
    mock_stdin.isatty.return_value = True
    mock_stdin.fileno.return_value = 0  # Assume 0 is a valid file descriptor

    # Mock os.dup to raise an OSError
    mocker.patch('os.dup', side_effect=OSError)

    # Mock os.fdopen to prevent actually opening file descriptors
    mocker.patch('os.fdopen')

    # Mock os.devnull to prevent opening the actual devnull
    mocker.patch('os.devnull', new_callable=mocker.PropertyMock(return_value='/dev/null'))

    # Mock open to prevent opening the actual devnull
    mock_open = mocker.patch('builtins.open', mocker.mock_open())

    # Call _save_stdin on the worker_process
    worker_process._save_stdin()

    # Assert that open was called with os.devnull
    mock_open.assert_called_once_with('/dev/null')

def test_worker_process_save_stdin_not_tty(mock_stdin, worker_process, mocker):
    # Setup the mock for sys.stdin to simulate not isatty()
    mock_stdin.isatty.return_value = False

    # Mock os.devnull to prevent opening the actual devnull
    mocker.patch('os.devnull', new_callable=mocker.PropertyMock(return_value='/dev/null'))

    # Mock open to prevent opening the actual devnull
    mock_open = mocker.patch('builtins.open', mocker.mock_open())

    # Call _save_stdin on the worker_process
    worker_process._save_stdin()

    # Assert that open was called with os.devnull
    mock_open.assert_called_once_with('/dev/null')

def test_worker_process_save_stdin_tty_with_invalid_fileno(mock_stdin, worker_process, mocker):
    # Setup the mock for sys.stdin to simulate isatty() and fileno()
    mock_stdin.isatty.return_value = True
    mock_stdin.fileno.side_effect = ValueError  # Simulate invalid fileno

    # Mock os.devnull to prevent opening the actual devnull
    mocker.patch('os.devnull', new_callable=mocker.PropertyMock(return_value='/dev/null'))

    # Mock open to prevent opening the actual devnull
    mock_open = mocker.patch('builtins.open', mocker.mock_open())

    # Call _save_stdin on the worker_process
    worker_process._save_stdin()

    # Assert that open was called with os.devnull
    mock_open.assert_called_once_with('/dev/null')
