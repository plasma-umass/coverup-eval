# file lib/ansible/executor/process/worker.py:95-111
# lines [95, 103, 104, 105, 109, 111]
# branches []

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.executor.process.worker import WorkerProcess
from ansible.utils.display import Display

# Mock the Display class to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'debug')

# Test function to cover the _hard_exit method
def test_worker_process_hard_exit(mock_display):
    # Create a MagicMock object for each required argument
    final_q = MagicMock()
    task_vars = MagicMock()
    host = MagicMock()
    task = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    variable_manager = MagicMock()
    shared_loader_obj = MagicMock()

    # Instantiate WorkerProcess with all required mocked arguments
    worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)

    with patch.object(os, '_exit') as mock_exit:
        worker._hard_exit(Exception("Test Exception"))
        mock_exit.assert_called_once_with(1)

    # Ensure that the debug method was called
    assert Display.debug.called
    Display.debug.assert_called_with(u"WORKER HARD EXIT: Test Exception")

    # Cleanup: No cleanup required as we are mocking os._exit and Display.debug
