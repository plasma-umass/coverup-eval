# file tqdm/contrib/utils_worker.py:15-40
# lines [21, 22, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40]
# branches ['27->28', '27->34', '29->30', '29->34', '30->31', '30->33']

import pytest
from concurrent.futures import ThreadPoolExecutor, Future
from collections import deque
from unittest.mock import Mock
from tqdm.contrib.utils_worker import MonoWorker

def test_mono_worker_submit_and_cancel(mocker):
    mocker.patch('tqdm.contrib.utils_worker.tqdm_auto')

    worker = MonoWorker()

    # Mock a long running function
    def long_running_function():
        import time
        time.sleep(0.1)

    # Submit a long running task to fill the queue
    future1 = worker.submit(long_running_function)
    assert len(worker.futures) == 1

    # Submit another task to fill the queue and trigger maxlen condition
    future2 = worker.submit(long_running_function)
    assert len(worker.futures) == 2

    # Submit a third task to trigger the cancellation of the waiting task
    future3 = worker.submit(long_running_function)
    assert len(worker.futures) == 2
    assert worker.futures[0] == future1
    assert worker.futures[1] == future3
    assert future2.cancelled()

    # Clean up
    future1.cancel()
    future3.cancel()
    worker.pool.shutdown(wait=False)

def test_mono_worker_exception_during_submit(mocker):
    write_mock = mocker.patch('tqdm.contrib.utils_worker.tqdm_auto.write')

    worker = MonoWorker()

    # Mock ThreadPoolExecutor to raise an exception on submit
    mock_pool = mocker.patch.object(worker, 'pool', autospec=True)
    mock_pool.submit.side_effect = Exception("Test exception")

    # Submit a task to trigger the exception
    worker.submit(lambda: None)
    # Check if the exception was written to tqdm_auto
    write_mock.assert_called_with("Test exception")

    # Clean up
    worker.pool.shutdown(wait=False)

# Run the tests
pytest.main()
