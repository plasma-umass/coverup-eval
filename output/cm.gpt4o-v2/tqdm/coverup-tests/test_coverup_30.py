# file: tqdm/contrib/utils_worker.py:15-40
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40], "branches": [[27, 28], [27, 34], [29, 30], [29, 34], [30, 31], [30, 33]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40], "branches": [[27, 28], [27, 34], [29, 30], [30, 31]]}

import pytest
from unittest.mock import Mock
from concurrent.futures import Future
from tqdm.contrib.utils_worker import MonoWorker
from tqdm import tqdm

def test_submit_replaces_waiting_task(monkeypatch):
    worker = MonoWorker()
    
    # Mocking the function to be submitted
    mock_func = Mock()
    
    # Creating a future that is not done
    future_running = Future()
    future_running.set_running_or_notify_cancel()
    
    # Creating a future that is done
    future_done = Future()
    future_done.set_result(None)
    
    # Patching the pool's submit method to return our mock futures
    monkeypatch.setattr(worker.pool, 'submit', Mock(side_effect=[future_running, future_done, future_done]))
    
    # Submitting the first task, which should be running
    worker.submit(mock_func)
    
    # Submitting the second task, which should replace the waiting task
    worker.submit(mock_func)
    
    # Submitting the third task, which should replace the waiting task again
    worker.submit(mock_func)
    
    # Assertions to ensure the correct behavior
    assert len(worker.futures) == 2
    assert worker.futures[0] == future_running
    assert worker.futures[1] == future_done
    assert future_running.cancelled() == False
    assert future_done.cancelled() == False

def test_submit_handles_exception(monkeypatch):
    worker = MonoWorker()
    
    # Mocking the function to be submitted
    mock_func = Mock()
    
    # Patching the pool's submit method to raise an exception
    monkeypatch.setattr(worker.pool, 'submit', Mock(side_effect=Exception("Test Exception")))
    
    # Patching tqdm.write to a mock to capture the output
    mock_tqdm_write = Mock()
    monkeypatch.setattr(tqdm, 'write', mock_tqdm_write)
    
    # Submitting the task, which should raise an exception
    worker.submit(mock_func)
    
    # Assertions to ensure the correct behavior
    mock_tqdm_write.assert_called_once_with("Test Exception")
    assert len(worker.futures) == 0
