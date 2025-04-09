# file: tornado/netutil.py:462-502
# asked: {"lines": [462, 463, 483, 484, 486, 487, 488, 490, 491, 494, 495, 498, 499, 500, 501, 502], "branches": [[495, 498], [495, 499], [499, 500], [499, 502]]}
# gained: {"lines": [462, 463, 483, 484, 486, 487, 488, 490, 491, 494, 495, 498, 499, 500, 501, 502], "branches": [[495, 498], [495, 499], [499, 500], [499, 502]]}

import pytest
import concurrent.futures
import os
from tornado.netutil import ThreadedResolver

@pytest.fixture
def reset_threadpool():
    # Save the original state
    original_threadpool = ThreadedResolver._threadpool
    original_threadpool_pid = ThreadedResolver._threadpool_pid
    yield
    # Restore the original state
    ThreadedResolver._threadpool = original_threadpool
    ThreadedResolver._threadpool_pid = original_threadpool_pid

def test_threaded_resolver_initialize(reset_threadpool):
    resolver = ThreadedResolver()
    resolver.initialize(num_threads=5)
    assert isinstance(ThreadedResolver._threadpool, concurrent.futures.ThreadPoolExecutor)
    assert ThreadedResolver._threadpool_pid == os.getpid()

def test_threaded_resolver_create_threadpool(reset_threadpool):
    # Test creating a new threadpool
    threadpool = ThreadedResolver._create_threadpool(num_threads=5)
    assert isinstance(threadpool, concurrent.futures.ThreadPoolExecutor)
    assert ThreadedResolver._threadpool_pid == os.getpid()

    # Test reusing the existing threadpool
    same_threadpool = ThreadedResolver._create_threadpool(num_threads=10)
    assert same_threadpool is threadpool

    # Simulate a fork by changing the PID
    ThreadedResolver._threadpool_pid = -1
    new_threadpool = ThreadedResolver._create_threadpool(num_threads=10)
    assert new_threadpool is not threadpool
    assert isinstance(new_threadpool, concurrent.futures.ThreadPoolExecutor)
    assert ThreadedResolver._threadpool_pid == os.getpid()
