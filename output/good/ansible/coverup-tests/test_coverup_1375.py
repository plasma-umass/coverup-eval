# file lib/ansible/executor/process/worker.py:80-93
# lines [89, 90, 91, 93]
# branches []

import pytest
import os
import sys
from unittest.mock import MagicMock
from ansible.executor.process.worker import WorkerProcess

# Mock class to replace WorkerProcess for testing
class MockWorkerProcess(WorkerProcess):
    def __init__(self):
        # Mock the required arguments for WorkerProcess
        super().__init__(
            final_q=MagicMock(),
            task_vars={},
            host=MagicMock(),
            task=MagicMock(),
            play_context=MagicMock(),
            loader=MagicMock(),
            variable_manager=MagicMock(),
            shared_loader_obj=MagicMock()
        )
        self._new_stdin = MagicMock()

    def _save_stdin(self):
        # Override to prevent actual file operations
        pass

    def run(self):
        pass  # Override run to prevent actual process execution

@pytest.fixture
def mock_worker_process(mocker):
    mocker.patch.object(WorkerProcess, '_save_stdin')
    mocker.patch.object(WorkerProcess, 'run')
    return MockWorkerProcess()

def test_worker_process_start_closes_new_stdin(mock_worker_process):
    mock_worker_process.start()
    mock_worker_process._new_stdin.close.assert_called_once()
