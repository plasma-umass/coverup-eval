# file: lib/ansible/executor/process/worker.py:216-219
# asked: {"lines": [216, 219], "branches": []}
# gained: {"lines": [216, 219], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.executor.process.worker import WorkerProcess

@pytest.fixture
def worker_process():
    loader = MagicMock()
    loader.cleanup_all_tmp_files = MagicMock()
    worker = WorkerProcess(
        final_q=MagicMock(),
        task_vars=MagicMock(),
        host=MagicMock(),
        task=MagicMock(),
        play_context=MagicMock(),
        loader=loader,
        variable_manager=MagicMock(),
        shared_loader_obj=MagicMock()
    )
    return worker

def test_worker_process_cleanup(worker_process):
    worker_process._clean_up()
    worker_process._loader.cleanup_all_tmp_files.assert_called_once()
