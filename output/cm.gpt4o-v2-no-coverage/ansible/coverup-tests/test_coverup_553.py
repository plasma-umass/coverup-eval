# file: lib/ansible/executor/process/worker.py:113-138
# asked: {"lines": [113, 123, 124, 125, 126, 137, 138], "branches": [[137, 0], [137, 138]]}
# gained: {"lines": [113, 123, 124, 125, 126, 137, 138], "branches": [[137, 138]]}

import pytest
import sys
import os
from unittest.mock import MagicMock, patch
from ansible.executor.process.worker import WorkerProcess

@pytest.fixture
def worker_process():
    final_q = MagicMock()
    task_vars = MagicMock()
    host = MagicMock()
    task = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    variable_manager = MagicMock()
    shared_loader_obj = MagicMock()
    worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    worker._run = MagicMock()
    worker._hard_exit = MagicMock()
    return worker

def test_worker_process_run_success(worker_process):
    worker_process._run.return_value = "success"
    with patch('sys.stdout', new_callable=MagicMock()) as mock_stdout, \
         patch('sys.stderr', new_callable=MagicMock()) as mock_stderr:
        result = worker_process.run()
        assert result == "success"
        if sys.version_info[0] >= 3:
            mock_stdout.write.assert_not_called()
            mock_stderr.write.assert_not_called()

def test_worker_process_run_exception(worker_process):
    worker_process._run.side_effect = Exception("test exception")
    with patch('sys.stdout', new_callable=MagicMock()) as mock_stdout, \
         patch('sys.stderr', new_callable=MagicMock()) as mock_stderr:
        worker_process.run()
        worker_process._hard_exit.assert_called_once()
        if sys.version_info[0] >= 3:
            mock_stdout.write.assert_not_called()
            mock_stderr.write.assert_not_called()

def test_worker_process_run_base_exception(worker_process):
    worker_process._run.side_effect = BaseException("test base exception")
    with patch('sys.stdout', new_callable=MagicMock()) as mock_stdout, \
         patch('sys.stderr', new_callable=MagicMock()) as mock_stderr:
        worker_process.run()
        worker_process._hard_exit.assert_called_once()
        if sys.version_info[0] >= 3:
            mock_stdout.write.assert_not_called()
            mock_stderr.write.assert_not_called()
