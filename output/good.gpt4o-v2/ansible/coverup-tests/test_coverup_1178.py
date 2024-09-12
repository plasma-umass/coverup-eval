# file: lib/ansible/executor/process/worker.py:63-78
# asked: {"lines": [64, 65, 66, 67, 68, 69, 72, 73, 75, 77, 78], "branches": [[66, 67], [66, 77], [77, 0], [77, 78]]}
# gained: {"lines": [64, 65, 66, 67, 68, 69, 72, 73, 75, 77, 78], "branches": [[66, 67], [66, 77], [77, 0], [77, 78]]}

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

def test_save_stdin_isatty_true(monkeypatch, worker_process):
    mock_stdin = mock.Mock()
    mock_stdin.isatty.return_value = True
    mock_stdin.fileno.side_effect = [0, 0]  # Simulate fileno being called twice

    monkeypatch.setattr(sys, 'stdin', mock_stdin)
    monkeypatch.setattr(os, 'dup', lambda x: x)
    mock_fdopen = mock.mock_open()
    monkeypatch.setattr(os, 'fdopen', mock_fdopen)

    worker_process._save_stdin()

    mock_stdin.isatty.assert_called_once()
    assert mock_stdin.fileno.call_count == 2
    mock_fdopen.assert_called_once_with(0)
    assert worker_process._new_stdin == mock_fdopen()

def test_save_stdin_isatty_false(monkeypatch, worker_process):
    mock_stdin = mock.Mock()
    mock_stdin.isatty.return_value = False

    monkeypatch.setattr(sys, 'stdin', mock_stdin)

    worker_process._save_stdin()

    mock_stdin.isatty.assert_called_once()
    assert worker_process._new_stdin is not None
    assert worker_process._new_stdin.name == os.devnull

def test_save_stdin_oserror(monkeypatch, worker_process):
    mock_stdin = mock.Mock()
    mock_stdin.isatty.return_value = True
    mock_stdin.fileno.side_effect = [0, 0]  # Simulate fileno being called twice

    monkeypatch.setattr(sys, 'stdin', mock_stdin)
    monkeypatch.setattr(os, 'dup', mock.Mock(side_effect=OSError))

    worker_process._save_stdin()

    mock_stdin.isatty.assert_called_once()
    assert mock_stdin.fileno.call_count == 2
    assert worker_process._new_stdin is not None
    assert worker_process._new_stdin.name == os.devnull

def test_save_stdin_attributeerror(monkeypatch, worker_process):
    mock_stdin = mock.Mock()
    mock_stdin.isatty.side_effect = AttributeError

    monkeypatch.setattr(sys, 'stdin', mock_stdin)

    worker_process._save_stdin()

    mock_stdin.isatty.assert_called_once()
    assert worker_process._new_stdin is not None
    assert worker_process._new_stdin.name == os.devnull

def test_save_stdin_valueerror(monkeypatch, worker_process):
    mock_stdin = mock.Mock()
    mock_stdin.isatty.side_effect = ValueError

    monkeypatch.setattr(sys, 'stdin', mock_stdin)

    worker_process._save_stdin()

    mock_stdin.isatty.assert_called_once()
    assert worker_process._new_stdin is not None
    assert worker_process._new_stdin.name == os.devnull
