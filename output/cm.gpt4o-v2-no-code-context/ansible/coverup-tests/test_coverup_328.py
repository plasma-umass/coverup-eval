# file: lib/ansible/executor/process/worker.py:46-61
# asked: {"lines": [46, 48, 50, 51, 52, 53, 54, 55, 56, 57, 61], "branches": []}
# gained: {"lines": [46, 48, 50, 51, 52, 53, 54, 55, 56, 57, 61], "branches": []}

import pytest
from unittest.mock import Mock, patch
from multiprocessing import get_context

# Assuming the WorkerProcess class is imported from ansible.executor.process.worker
from ansible.executor.process.worker import WorkerProcess

@pytest.fixture
def mock_loader():
    loader = Mock()
    loader._tempfiles = set()
    return loader

def test_worker_process_initialization(mock_loader):
    final_q = Mock()
    task_vars = Mock()
    host = Mock()
    task = Mock()
    play_context = Mock()
    variable_manager = Mock()
    shared_loader_obj = Mock()

    with patch('ansible.executor.process.worker.multiprocessing_context', get_context('fork')):
        worker = WorkerProcess(final_q, task_vars, host, task, play_context, mock_loader, variable_manager, shared_loader_obj)

    assert worker._final_q == final_q
    assert worker._task_vars == task_vars
    assert worker._host == host
    assert worker._task == task
    assert worker._play_context == play_context
    assert worker._loader == mock_loader
    assert worker._variable_manager == variable_manager
    assert worker._shared_loader_obj == shared_loader_obj
    assert worker._loader._tempfiles == set()
