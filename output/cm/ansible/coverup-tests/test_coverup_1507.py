# file lib/ansible/executor/process/worker.py:216-219
# lines [219]
# branches []

import pytest
from ansible.executor.process.worker import WorkerProcess
from multiprocessing import get_context
from unittest.mock import MagicMock

@pytest.fixture
def mock_loader(mocker):
    mock_loader = MagicMock()
    mock_loader.cleanup_all_tmp_files = MagicMock()
    # Mock the _tempfiles attribute to prevent AttributeError
    mock_loader._tempfiles = set()
    return mock_loader

@pytest.fixture
def worker_process(mock_loader):
    # Use the 'fork' context for multiprocessing to ensure compatibility with MagicMock
    ctx = get_context('fork')
    # Create a WorkerProcess with the correct number of arguments
    worker = WorkerProcess(None, None, None, None, None, mock_loader, None, ctx)
    yield worker
    # Cleanup code if necessary

def test_worker_process_clean_up(worker_process):
    worker_process._clean_up()
    worker_process._loader.cleanup_all_tmp_files.assert_called_once()
