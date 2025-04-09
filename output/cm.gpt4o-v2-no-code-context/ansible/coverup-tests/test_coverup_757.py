# file: lib/ansible/executor/process/worker.py:216-219
# asked: {"lines": [216, 219], "branches": []}
# gained: {"lines": [216, 219], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from multiprocessing import get_context

# Assuming the WorkerProcess class is defined in ansible/executor/process/worker.py
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
    worker._loader = loader
    return worker

def test_worker_process_cleanup(worker_process):
    worker_process._clean_up()
    worker_process._loader.cleanup_all_tmp_files.assert_called_once()
