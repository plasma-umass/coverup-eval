# file: lib/ansible/executor/process/worker.py:63-78
# asked: {"lines": [63, 64, 65, 66, 67, 68, 69, 72, 73, 75, 77, 78], "branches": [[66, 67], [66, 77], [77, 0], [77, 78]]}
# gained: {"lines": [63, 64, 65, 66, 67, 68, 69, 72, 73, 75, 77, 78], "branches": [[66, 67], [66, 77], [77, 0], [77, 78]]}

import os
import sys
import pytest
from unittest import mock
from ansible.executor.process.worker import WorkerProcess

@pytest.fixture
def worker_process():
    return WorkerProcess(
        final_q=mock.Mock(),
        task_vars=mock.Mock(),
        host=mock.Mock(),
        task=mock.Mock(),
        play_context=mock.Mock(),
        loader=mock.Mock(),
        variable_manager=mock.Mock(),
        shared_loader_obj=mock.Mock()
    )

def test_save_stdin_tty(worker_process, monkeypatch):
    mock_stdin = mock.Mock()
    mock_stdin.isatty.return_value = True
    mock_stdin.fileno.return_value = 0

    monkeypatch.setattr(sys, 'stdin', mock_stdin)
    monkeypatch.setattr(os, 'dup', lambda x: x)
    mock_fdopen = mock.Mock()
    monkeypatch.setattr(os, 'fdopen', mock_fdopen)

    worker_process._save_stdin()

    mock_stdin.isatty.assert_called_once()
    assert mock_stdin.fileno.call_count == 2  # Adjusted to 2 because fileno is called twice
    mock_fdopen.assert_called_once_with(0)
    assert worker_process._new_stdin == mock_fdopen()

def test_save_stdin_not_tty(worker_process, monkeypatch):
    mock_stdin = mock.Mock()
    mock_stdin.isatty.return_value = False

    monkeypatch.setattr(sys, 'stdin', mock_stdin)
    mock_open = mock.mock_open()
    monkeypatch.setattr('builtins.open', mock_open)

    worker_process._save_stdin()

    mock_stdin.isatty.assert_called_once()
    mock_open.assert_called_once_with(os.devnull)
    assert worker_process._new_stdin == mock_open()

def test_save_stdin_oserror(worker_process, monkeypatch):
    mock_stdin = mock.Mock()
    mock_stdin.isatty.return_value = True
    mock_stdin.fileno.return_value = 0

    monkeypatch.setattr(sys, 'stdin', mock_stdin)
    monkeypatch.setattr(os, 'dup', mock.Mock(side_effect=OSError))
    mock_open = mock.mock_open()
    monkeypatch.setattr('builtins.open', mock_open)

    worker_process._save_stdin()

    mock_stdin.isatty.assert_called_once()
    assert mock_stdin.fileno.call_count == 2  # Adjusted to 2 because fileno is called twice
    mock_open.assert_called_once_with(os.devnull)
    assert worker_process._new_stdin == mock_open()

def test_save_stdin_attributeerror(worker_process, monkeypatch):
    mock_stdin = mock.Mock()
    mock_stdin.isatty.side_effect = AttributeError

    monkeypatch.setattr(sys, 'stdin', mock_stdin)
    mock_open = mock.mock_open()
    monkeypatch.setattr('builtins.open', mock_open)

    worker_process._save_stdin()

    mock_stdin.isatty.assert_called_once()
    mock_open.assert_called_once_with(os.devnull)
    assert worker_process._new_stdin == mock_open()

def test_save_stdin_valueerror(worker_process, monkeypatch):
    mock_stdin = mock.Mock()
    mock_stdin.isatty.side_effect = ValueError

    monkeypatch.setattr(sys, 'stdin', mock_stdin)
    mock_open = mock.mock_open()
    monkeypatch.setattr('builtins.open', mock_open)

    worker_process._save_stdin()

    mock_stdin.isatty.assert_called_once()
    mock_open.assert_called_once_with(os.devnull)
    assert worker_process._new_stdin == mock_open()
