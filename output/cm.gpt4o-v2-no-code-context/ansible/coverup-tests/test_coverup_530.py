# file: lib/ansible/executor/process/worker.py:95-111
# asked: {"lines": [95, 103, 104, 105, 109, 111], "branches": []}
# gained: {"lines": [95, 103, 104, 105, 109, 111], "branches": []}

import pytest
import os
from unittest import mock
from ansible.executor.process.worker import WorkerProcess

def test_worker_process_hard_exit(monkeypatch):
    # Mock the display.debug method to avoid actual logging
    mock_display_debug = mock.Mock()
    monkeypatch.setattr('ansible.executor.process.worker.display.debug', mock_display_debug)

    # Mock the required arguments for WorkerProcess
    mock_final_q = mock.Mock()
    mock_task_vars = mock.Mock()
    mock_host = mock.Mock()
    mock_task = mock.Mock()
    mock_play_context = mock.Mock()
    mock_loader = mock.Mock()
    mock_variable_manager = mock.Mock()
    mock_shared_loader_obj = mock.Mock()

    # Create an instance of WorkerProcess with mocked arguments
    worker_process = WorkerProcess(
        final_q=mock_final_q,
        task_vars=mock_task_vars,
        host=mock_host,
        task=mock_task,
        play_context=mock_play_context,
        loader=mock_loader,
        variable_manager=mock_variable_manager,
        shared_loader_obj=mock_shared_loader_obj
    )

    # Mock os._exit to avoid actually exiting the test runner
    mock_os_exit = mock.Mock()
    monkeypatch.setattr(os, '_exit', mock_os_exit)

    # Create a test exception
    test_exception = Exception("Test Exception")

    # Call the _hard_exit method with the test exception
    worker_process._hard_exit(test_exception)

    # Assert that display.debug was called with the correct message
    mock_display_debug.assert_called_once_with(u"WORKER HARD EXIT: Test Exception")

    # Assert that os._exit was called with the correct exit code
    mock_os_exit.assert_called_once_with(1)

def test_worker_process_hard_exit_with_ioerror(monkeypatch):
    # Mock the display.debug method to raise an IOError
    def mock_display_debug_raises(*args, **kwargs):
        raise IOError("Test IOError")
    monkeypatch.setattr('ansible.executor.process.worker.display.debug', mock_display_debug_raises)

    # Mock the required arguments for WorkerProcess
    mock_final_q = mock.Mock()
    mock_task_vars = mock.Mock()
    mock_host = mock.Mock()
    mock_task = mock.Mock()
    mock_play_context = mock.Mock()
    mock_loader = mock.Mock()
    mock_variable_manager = mock.Mock()
    mock_shared_loader_obj = mock.Mock()

    # Create an instance of WorkerProcess with mocked arguments
    worker_process = WorkerProcess(
        final_q=mock_final_q,
        task_vars=mock_task_vars,
        host=mock_host,
        task=mock_task,
        play_context=mock_play_context,
        loader=mock_loader,
        variable_manager=mock_variable_manager,
        shared_loader_obj=mock_shared_loader_obj
    )

    # Mock os._exit to avoid actually exiting the test runner
    mock_os_exit = mock.Mock()
    monkeypatch.setattr(os, '_exit', mock_os_exit)

    # Create a test exception
    test_exception = Exception("Test Exception")

    # Call the _hard_exit method with the test exception
    worker_process._hard_exit(test_exception)

    # Assert that os._exit was called with the correct exit code
    mock_os_exit.assert_called_once_with(1)
