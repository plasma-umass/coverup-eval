# file: lib/ansible/executor/process/worker.py:216-219
# asked: {"lines": [216, 219], "branches": []}
# gained: {"lines": [216, 219], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.executor.process.worker import WorkerProcess
from ansible.utils.multiprocessing import context as multiprocessing_context

class MockLoader:
    def __init__(self):
        self._tempfiles = set()

    def cleanup_all_tmp_files(self):
        self._tempfiles.clear()

@pytest.fixture
def worker_process():
    loader = MockLoader()
    return WorkerProcess(
        final_q=MagicMock(),
        task_vars=MagicMock(),
        host=MagicMock(),
        task=MagicMock(),
        play_context=MagicMock(),
        loader=loader,
        variable_manager=MagicMock(),
        shared_loader_obj=MagicMock()
    )

def test_clean_up(worker_process):
    # Add a temporary file to the loader
    worker_process._loader._tempfiles.add('tempfile1')
    worker_process._loader._tempfiles.add('tempfile2')

    # Ensure the temporary files are present
    assert len(worker_process._loader._tempfiles) == 2

    # Call the _clean_up method
    worker_process._clean_up()

    # Ensure the temporary files have been cleaned up
    assert len(worker_process._loader._tempfiles) == 0
