# file: lib/ansible/executor/process/worker.py:46-61
# asked: {"lines": [46, 48, 50, 51, 52, 53, 54, 55, 56, 57, 61], "branches": []}
# gained: {"lines": [46, 48, 50, 51, 52, 53, 54, 55, 56, 57, 61], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.executor.process.worker import WorkerProcess
from ansible.utils.multiprocessing import context as multiprocessing_context

@pytest.fixture
def worker_process():
    final_q = Mock()
    task_vars = Mock()
    host = Mock()
    task = Mock()
    play_context = Mock()
    loader = Mock()
    variable_manager = Mock()
    shared_loader_obj = Mock()
    return WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)

def test_worker_process_init(worker_process):
    assert worker_process._final_q is not None
    assert worker_process._task_vars is not None
    assert worker_process._host is not None
    assert worker_process._task is not None
    assert worker_process._play_context is not None
    assert worker_process._loader is not None
    assert worker_process._variable_manager is not None
    assert worker_process._shared_loader_obj is not None
    assert worker_process._loader._tempfiles == set()
