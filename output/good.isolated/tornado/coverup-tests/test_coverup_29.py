# file tornado/netutil.py:462-502
# lines [462, 463, 483, 484, 486, 487, 488, 490, 491, 494, 495, 498, 499, 500, 501, 502]
# branches ['495->498', '495->499', '499->500', '499->502']

import os
import pytest
import concurrent.futures
from unittest.mock import patch
from tornado.netutil import ThreadedResolver

@pytest.fixture
def cleanup_threadpool():
    # Fixture to clean up the threadpool after the test
    yield
    ThreadedResolver._threadpool = None
    ThreadedResolver._threadpool_pid = None

def test_threaded_resolver_create_threadpool(cleanup_threadpool, mocker):
    # Mock os.getpid to simulate fork
    mocker.patch('os.getpid', return_value=1234)
    # Ensure the threadpool is None to begin with
    assert ThreadedResolver._threadpool is None
    assert ThreadedResolver._threadpool_pid is None

    # Create a threadpool
    threadpool = ThreadedResolver._create_threadpool(5)
    assert isinstance(threadpool, concurrent.futures.ThreadPoolExecutor)
    assert ThreadedResolver._threadpool is threadpool
    assert ThreadedResolver._threadpool_pid == 1234

    # Simulate a fork by changing the PID
    os.getpid.return_value = 5678
    # Create a new threadpool after the "fork"
    new_threadpool = ThreadedResolver._create_threadpool(5)
    assert isinstance(new_threadpool, concurrent.futures.ThreadPoolExecutor)
    assert new_threadpool is not threadpool
    assert ThreadedResolver._threadpool is new_threadpool
    assert ThreadedResolver._threadpool_pid == 5678

    # Verify that the same threadpool is returned if the PID hasn't changed
    same_threadpool = ThreadedResolver._create_threadpool(5)
    assert same_threadpool is new_threadpool
