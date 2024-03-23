# file lib/ansible/executor/process/worker.py:46-61
# lines [46, 48, 50, 51, 52, 53, 54, 55, 56, 57, 61]
# branches []

import pytest
from unittest.mock import MagicMock, patch
from multiprocessing import get_context
from ansible.executor.process.worker import WorkerProcess

# Define the test function
def test_worker_process_initialization():
    # Mock the multiprocessing context
    multiprocessing_context = get_context('fork')

    # Create mock objects for the WorkerProcess constructor arguments
    final_q = multiprocessing_context.Queue()
    task_vars = {}
    host = MagicMock()
    task = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    variable_manager = MagicMock()
    shared_loader_obj = MagicMock()

    # Patch the multiprocessing_context.Process to prevent actual process creation
    with patch('ansible.executor.process.worker.multiprocessing_context.Process'):
        # Initialize the WorkerProcess
        worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)

    # Assertions to verify postconditions
    assert worker._final_q == final_q
    assert worker._task_vars == task_vars
    assert worker._host == host
    assert worker._task == task
    assert worker._play_context == play_context
    assert worker._loader == loader
    assert worker._variable_manager == variable_manager
    assert worker._shared_loader_obj == shared_loader_obj
    assert worker._loader._tempfiles == set()

    # Clean up
    final_q.close()
    final_q.join_thread()

# Run the test function
def test_module():
    test_worker_process_initialization()
