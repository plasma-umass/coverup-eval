# file: lib/ansible/executor/process/worker.py:63-78
# asked: {"lines": [63, 64, 65, 66, 67, 68, 69, 72, 73, 75, 77, 78], "branches": [[66, 67], [66, 77], [77, 0], [77, 78]]}
# gained: {"lines": [63, 64, 65, 66, 67, 68, 69, 72, 73, 75, 77, 78], "branches": [[66, 67], [66, 77], [77, 0], [77, 78]]}

import pytest
import sys
import os
from unittest import mock
from ansible.executor.process.worker import WorkerProcess

class MockWorkerProcess(WorkerProcess):
    def __init__(self):
        pass

@pytest.fixture
def worker_process():
    return MockWorkerProcess()

def test_save_stdin_tty(worker_process, monkeypatch):
    mock_stdin = mock.Mock()
    mock_stdin.isatty.return_value = True
    mock_stdin.fileno.return_value = 0

    monkeypatch.setattr(sys, 'stdin', mock_stdin)
    monkeypatch.setattr(os, 'dup', lambda x: 0)
    monkeypatch.setattr(os, 'fdopen', lambda x: mock_stdin)

    worker_process._save_stdin()

    assert worker_process._new_stdin == mock_stdin

def test_save_stdin_not_tty(worker_process, monkeypatch):
    mock_stdin = mock.Mock()
    mock_stdin.isatty.return_value = False

    monkeypatch.setattr(sys, 'stdin', mock_stdin)

    worker_process._save_stdin()

    assert worker_process._new_stdin is not None
    assert worker_process._new_stdin.name == os.devnull

def test_save_stdin_oserror(worker_process, monkeypatch):
    mock_stdin = mock.Mock()
    mock_stdin.isatty.return_value = True
    mock_stdin.fileno.return_value = 0

    monkeypatch.setattr(sys, 'stdin', mock_stdin)
    monkeypatch.setattr(os, 'dup', mock.Mock(side_effect=OSError))

    worker_process._save_stdin()

    assert worker_process._new_stdin is not None
    assert worker_process._new_stdin.name == os.devnull

def test_save_stdin_attributeerror(worker_process, monkeypatch):
    mock_stdin = mock.Mock()
    mock_stdin.isatty.side_effect = AttributeError

    monkeypatch.setattr(sys, 'stdin', mock_stdin)

    worker_process._save_stdin()

    assert worker_process._new_stdin is not None
    assert worker_process._new_stdin.name == os.devnull

def test_save_stdin_valueerror(worker_process, monkeypatch):
    mock_stdin = mock.Mock()
    mock_stdin.isatty.side_effect = ValueError

    monkeypatch.setattr(sys, 'stdin', mock_stdin)

    worker_process._save_stdin()

    assert worker_process._new_stdin is not None
    assert worker_process._new_stdin.name == os.devnull
