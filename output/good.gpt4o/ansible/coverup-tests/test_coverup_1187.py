# file lib/ansible/executor/process/worker.py:113-138
# lines [123, 124, 125, 126, 137, 138]
# branches ['137->exit', '137->138']

import pytest
import sys
import os
from unittest.mock import patch, MagicMock
from multiprocessing import get_context

# Assuming the WorkerProcess class is imported from ansible.executor.process.worker
from ansible.executor.process.worker import WorkerProcess

@pytest.fixture
def mock_run_method(mocker):
    return mocker.patch.object(WorkerProcess, '_run', side_effect=Exception("Test Exception"))

@pytest.fixture
def mock_hard_exit_method(mocker):
    return mocker.patch.object(WorkerProcess, '_hard_exit')

@pytest.fixture
def worker_process():
    # Create a WorkerProcess instance with mock arguments
    final_q = MagicMock()
    task_vars = MagicMock()
    host = MagicMock()
    task = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    variable_manager = MagicMock()
    shared_loader_obj = MagicMock()
    return WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)

def test_worker_process_run_exception_handling(mock_run_method, mock_hard_exit_method, worker_process):
    # Run the worker process
    with patch('sys.stdout', new_callable=MagicMock()) as mock_stdout, \
         patch('sys.stderr', new_callable=MagicMock()) as mock_stderr:
        worker_process.run()

        # Check that _run was called and raised an exception
        mock_run_method.assert_called_once()

        # Check that _hard_exit was called with the exception
        mock_hard_exit_method.assert_called_once()
        assert mock_hard_exit_method.call_args[0][0].args[0] == "Test Exception"

        # Check that sys.stdout and sys.stderr were redirected to os.devnull
        if sys.version_info[0] >= 3:
            assert sys.stdout.name == os.devnull
            assert sys.stderr.name == os.devnull
