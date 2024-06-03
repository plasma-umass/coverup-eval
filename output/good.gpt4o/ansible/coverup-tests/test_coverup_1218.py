# file lib/ansible/executor/process/worker.py:95-111
# lines [103, 104, 105, 109, 111]
# branches []

import pytest
import os
from unittest import mock
from ansible.executor.process.worker import WorkerProcess

def test_worker_hard_exit(mocker):
    # Mock the display.debug method to raise an exception
    mock_display = mocker.patch('ansible.executor.process.worker.display.debug', side_effect=Exception("Mocked exception"))

    # Create a mock for the required arguments
    mock_final_q = mock.Mock()
    mock_task_vars = mock.Mock()
    mock_host = mock.Mock()
    mock_task = mock.Mock()
    mock_play_context = mock.Mock()
    mock_loader = mock.Mock()
    mock_variable_manager = mock.Mock()
    mock_shared_loader_obj = mock.Mock()

    # Create an instance of WorkerProcess with the mocked arguments
    worker = WorkerProcess(mock_final_q, mock_task_vars, mock_host, mock_task, mock_play_context, mock_loader, mock_variable_manager, mock_shared_loader_obj)

    # Mock os._exit to prevent the test from exiting
    mock_exit = mocker.patch('os._exit')

    # Call the _hard_exit method with a test exception
    test_exception = Exception("Test exception")
    worker._hard_exit(test_exception)

    # Assert that display.debug was called with the correct message
    mock_display.assert_called_once_with(u"WORKER HARD EXIT: %s" % str(test_exception))

    # Assert that os._exit was called with the correct exit code
    mock_exit.assert_called_once_with(1)
