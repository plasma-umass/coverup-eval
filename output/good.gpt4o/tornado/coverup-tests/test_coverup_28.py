# file tornado/netutil.py:462-502
# lines [462, 463, 483, 484, 486, 487, 488, 490, 491, 494, 495, 498, 499, 500, 501, 502]
# branches ['495->498', '495->499', '499->500', '499->502']

import pytest
import os
import concurrent.futures
from tornado.netutil import ThreadedResolver

@pytest.fixture
def reset_threadpool():
    # Save the original state
    original_threadpool = ThreadedResolver._threadpool
    original_threadpool_pid = ThreadedResolver._threadpool_pid
    # Reset the state before the test
    ThreadedResolver._threadpool = None
    ThreadedResolver._threadpool_pid = None
    yield
    # Restore the original state after the test
    ThreadedResolver._threadpool = original_threadpool
    ThreadedResolver._threadpool_pid = original_threadpool_pid

def test_threaded_resolver_create_threadpool(reset_threadpool):
    resolver = ThreadedResolver()
    
    # Simulate a fork by changing the pid
    original_pid = os.getpid()
    ThreadedResolver._threadpool_pid = original_pid + 1

    # Create a new threadpool after the fork
    resolver.initialize(num_threads=5)
    
    # Check if the threadpool is created with the correct number of threads
    assert isinstance(ThreadedResolver._threadpool, concurrent.futures.ThreadPoolExecutor)
    assert ThreadedResolver._threadpool._max_workers == 5
    assert ThreadedResolver._threadpool_pid == os.getpid()

    # Create a new threadpool without changing the pid
    resolver.initialize(num_threads=10)
    
    # Check if the threadpool is not recreated and retains the original number of threads
    assert isinstance(ThreadedResolver._threadpool, concurrent.futures.ThreadPoolExecutor)
    assert ThreadedResolver._threadpool._max_workers == 5
    assert ThreadedResolver._threadpool_pid == os.getpid()
