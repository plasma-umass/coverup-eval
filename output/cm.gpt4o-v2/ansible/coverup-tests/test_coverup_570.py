# file: lib/ansible/executor/process/worker.py:95-111
# asked: {"lines": [95, 103, 104, 105, 109, 111], "branches": []}
# gained: {"lines": [95, 103, 104, 105, 109, 111], "branches": []}

import pytest
import os
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

def test_hard_exit(worker_process, mocker):
    mock_display = mocker.patch('ansible.executor.process.worker.display')
    mock_os_exit = mocker.patch('os._exit')

    # Test the try block
    worker_process._hard_exit(Exception("Test Exception"))
    mock_display.debug.assert_called_once_with("WORKER HARD EXIT: Test Exception")
    mock_os_exit.assert_called_once_with(1)

    # Reset mocks
    mock_display.reset_mock()
    mock_os_exit.reset_mock()

    # Test the except block
    mock_display.debug.side_effect = IOError("Test IOError")
    worker_process._hard_exit(Exception("Test Exception"))
    mock_display.debug.assert_called_once_with("WORKER HARD EXIT: Test Exception")
    mock_os_exit.assert_called_once_with(1)
