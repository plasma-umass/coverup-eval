# file: lib/ansible/executor/process/worker.py:46-61
# asked: {"lines": [46, 48, 50, 51, 52, 53, 54, 55, 56, 57, 61], "branches": []}
# gained: {"lines": [46, 48, 50, 51, 52, 53, 54, 55, 56, 57, 61], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.executor.process.worker import WorkerProcess

@pytest.fixture
def worker_process_params():
    final_q = MagicMock()
    task_vars = MagicMock()
    host = MagicMock()
    task = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    variable_manager = MagicMock()
    shared_loader_obj = MagicMock()
    return final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj

def test_worker_process_init(worker_process_params):
    final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj = worker_process_params

    worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)

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
    del worker
