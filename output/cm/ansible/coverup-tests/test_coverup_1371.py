# file lib/ansible/executor/process/worker.py:95-111
# lines [103, 104, 105, 109, 111]
# branches []

import os
import pytest
from unittest.mock import Mock, patch
from ansible.executor.process.worker import WorkerProcess
from ansible.utils.display import Display

# Mock the Display class to raise an exception when debug is called
@pytest.fixture
def display_mock(mocker):
    mock_display = mocker.patch('ansible.executor.process.worker.display', spec=Display)
    mock_display.debug.side_effect = Exception("Mocked exception")
    return mock_display

# Test function to cover lines 103-111
def test_worker_process_hard_exit_with_exception(display_mock):
    # Mock all required arguments for WorkerProcess
    final_q = Mock()
    task_vars = {}
    host = Mock()
    task = Mock()
    play_context = Mock()
    loader = Mock()
    variable_manager = Mock()
    shared_loader_obj = Mock()

    # Instantiate WorkerProcess with all required mocked arguments
    worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)

    # Patch os._exit to prevent the test runner from actually exiting
    with patch.object(os, '_exit') as mock_exit:
        # Trigger the _hard_exit method
        worker._hard_exit(Exception("Test exception"))

        # Assert that os._exit was called with status code 1
        mock_exit.assert_called_once_with(1)

        # Assert that the debug method was called and raised an exception
        assert display_mock.debug.call_count == 1
        display_mock.debug.assert_called_with(u"WORKER HARD EXIT: Test exception")

# Run the test
def test_worker_process_hard_exit(display_mock):
    test_worker_process_hard_exit_with_exception(display_mock)
