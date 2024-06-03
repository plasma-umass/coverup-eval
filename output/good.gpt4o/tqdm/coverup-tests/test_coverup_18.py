# file tqdm/contrib/utils_worker.py:15-40
# lines [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40]
# branches ['27->28', '27->34', '29->30', '29->34', '30->31', '30->33']

import pytest
from unittest.mock import Mock
from concurrent.futures import ThreadPoolExecutor
from collections import deque
from tqdm.contrib.utils_worker import MonoWorker

def test_mono_worker_submit(mocker):
    # Mock tqdm_auto.write to avoid actual writing
    mocker.patch('tqdm.contrib.utils_worker.tqdm_auto.write')

    # Create a MonoWorker instance
    worker = MonoWorker()

    # Mock function to be submitted
    def mock_func(x):
        return x

    # Submit a task to fill the pool
    future1 = worker.submit(mock_func, 1)
    assert future1.result() == 1

    # Submit another task to replace the waiting task
    future2 = worker.submit(mock_func, 2)
    assert future2.result() == 2

    # Submit a third task to trigger the condition where the running task is re-inserted
    future3 = worker.submit(mock_func, 3)
    assert future3.result() == 3

    # Check that the futures deque has the correct length
    assert len(worker.futures) == 2

    # Check that the last submitted task is in the futures deque
    assert worker.futures[-1].result() == 3

    # Check that the first task is still running or completed
    assert worker.futures[0].result() in [1, 2]

    # Clean up by shutting down the ThreadPoolExecutor
    worker.pool.shutdown(wait=True)
