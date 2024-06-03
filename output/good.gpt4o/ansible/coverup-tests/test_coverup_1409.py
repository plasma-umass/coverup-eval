# file lib/ansible/executor/process/worker.py:63-78
# lines [64, 65, 66, 67, 68, 69, 72, 73, 75, 77, 78]
# branches ['66->67', '66->77', '77->exit', '77->78']

import pytest
import sys
import os
from unittest import mock
from ansible.executor.process.worker import WorkerProcess

@pytest.fixture
def mock_stdin_tty(mocker):
    mock_stdin = mocker.patch('sys.stdin')
    mock_stdin.isatty.return_value = True
    mock_stdin.fileno.return_value = 0
    return mock_stdin

@pytest.fixture
def mock_stdin_not_tty(mocker):
    mock_stdin = mocker.patch('sys.stdin')
    mock_stdin.isatty.return_value = False
    return mock_stdin

@pytest.fixture
def mock_stdin_no_fileno(mocker):
    mock_stdin = mocker.patch('sys.stdin')
    mock_stdin.isatty.return_value = True
    mock_stdin.fileno.side_effect = AttributeError
    return mock_stdin

@pytest.fixture
def mock_stdin_oserror(mocker):
    mock_stdin = mocker.patch('sys.stdin')
    mock_stdin.isatty.return_value = True
    mock_stdin.fileno.return_value = 0
    mocker.patch('os.fdopen', side_effect=OSError)
    return mock_stdin

def create_worker_process(mocker):
    mocker.patch('ansible.executor.process.worker.WorkerProcess.__init__', return_value=None)
    worker = WorkerProcess()
    worker.final_q = mock.Mock()
    worker.task_vars = mock.Mock()
    worker.host = mock.Mock()
    worker.task = mock.Mock()
    worker.play_context = mock.Mock()
    worker.loader = mock.Mock()
    worker.variable_manager = mock.Mock()
    worker.shared_loader_obj = mock.Mock()
    worker._new_stdin = None
    return worker

def test_save_stdin_tty(mock_stdin_tty, mocker):
    mocker.patch('os.fdopen', return_value='mocked_fd')
    worker = create_worker_process(mocker)
    worker._save_stdin()
    assert worker._new_stdin == 'mocked_fd'

def test_save_stdin_not_tty(mock_stdin_not_tty, mocker):
    mock_open = mocker.patch('builtins.open', mocker.mock_open())
    worker = create_worker_process(mocker)
    worker._save_stdin()
    mock_open.assert_called_once_with(os.devnull)
    assert worker._new_stdin == mock_open()

def test_save_stdin_no_fileno(mock_stdin_no_fileno, mocker):
    mock_open = mocker.patch('builtins.open', mocker.mock_open())
    worker = create_worker_process(mocker)
    worker._save_stdin()
    mock_open.assert_called_once_with(os.devnull)
    assert worker._new_stdin == mock_open()

def test_save_stdin_oserror(mock_stdin_oserror, mocker):
    mock_open = mocker.patch('builtins.open', mocker.mock_open())
    worker = create_worker_process(mocker)
    worker._save_stdin()
    mock_open.assert_called_once_with(os.devnull)
    assert worker._new_stdin == mock_open()
