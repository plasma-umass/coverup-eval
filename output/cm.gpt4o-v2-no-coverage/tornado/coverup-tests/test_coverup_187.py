# file: tornado/netutil.py:462-502
# asked: {"lines": [487, 488, 494, 495, 498, 499, 500, 501, 502], "branches": [[495, 498], [495, 499], [499, 500], [499, 502]]}
# gained: {"lines": [487, 488, 494, 495, 498, 499, 500, 501, 502], "branches": [[495, 498], [495, 499], [499, 500], [499, 502]]}

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

def test_initialize_creates_threadpool(reset_threadpool, monkeypatch):
    resolver = ThreadedResolver()
    
    # Ensure a new threadpool is created by simulating a different PID
    original_pid = os.getpid()
    monkeypatch.setattr(os, 'getpid', lambda: original_pid + 1)
    
    resolver.initialize(num_threads=5)
    assert isinstance(ThreadedResolver._threadpool, concurrent.futures.ThreadPoolExecutor)
    # We cannot directly access _max_workers, so we check the number of threads indirectly
    assert ThreadedResolver._threadpool._max_workers == 5

def test_create_threadpool_new_pid(reset_threadpool, monkeypatch):
    resolver = ThreadedResolver()
    resolver.initialize(num_threads=5)
    original_pid = os.getpid()
    
    # Simulate a fork by changing the PID
    monkeypatch.setattr(os, 'getpid', lambda: original_pid + 1)
    
    new_threadpool = ThreadedResolver._create_threadpool(3)
    assert new_threadpool._max_workers == 3
    assert ThreadedResolver._threadpool_pid == original_pid + 1

def test_create_threadpool_same_pid(reset_threadpool):
    resolver = ThreadedResolver()
    resolver.initialize(num_threads=5)
    original_threadpool = ThreadedResolver._threadpool
    original_pid = os.getpid()
    
    same_threadpool = ThreadedResolver._create_threadpool(3)
    assert same_threadpool == original_threadpool
    assert ThreadedResolver._threadpool_pid == original_pid
