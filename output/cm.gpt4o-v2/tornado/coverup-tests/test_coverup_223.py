# file: tornado/netutil.py:462-502
# asked: {"lines": [], "branches": [[495, 499], [499, 502]]}
# gained: {"lines": [], "branches": [[495, 499], [499, 502]]}

import pytest
import os
import concurrent.futures
from tornado.netutil import ThreadedResolver

def test_threaded_resolver_create_threadpool_new_pid(monkeypatch):
    # Ensure _threadpool and _threadpool_pid are reset
    ThreadedResolver._threadpool = None
    ThreadedResolver._threadpool_pid = None

    # Mock os.getpid to return a specific pid
    monkeypatch.setattr(os, "getpid", lambda: 12345)
    
    # Create threadpool with mocked pid
    threadpool = ThreadedResolver._create_threadpool(5)
    
    # Assertions to verify the threadpool is created and pid is set
    assert ThreadedResolver._threadpool is not None
    assert ThreadedResolver._threadpool_pid == 12345
    assert isinstance(threadpool, concurrent.futures.ThreadPoolExecutor)

def test_threaded_resolver_create_threadpool_existing_pid(monkeypatch):
    # Ensure _threadpool and _threadpool_pid are set
    ThreadedResolver._threadpool = concurrent.futures.ThreadPoolExecutor(5)
    ThreadedResolver._threadpool_pid = 12345

    # Mock os.getpid to return the same pid
    monkeypatch.setattr(os, "getpid", lambda: 12345)
    
    # Create threadpool with mocked pid
    threadpool = ThreadedResolver._create_threadpool(5)
    
    # Assertions to verify the existing threadpool is reused
    assert ThreadedResolver._threadpool is not None
    assert ThreadedResolver._threadpool_pid == 12345
    assert threadpool == ThreadedResolver._threadpool

def test_threaded_resolver_create_threadpool_different_pid(monkeypatch):
    # Ensure _threadpool and _threadpool_pid are set
    old_threadpool = concurrent.futures.ThreadPoolExecutor(5)
    ThreadedResolver._threadpool = old_threadpool
    ThreadedResolver._threadpool_pid = 12345

    # Mock os.getpid to return a different pid
    monkeypatch.setattr(os, "getpid", lambda: 67890)
    
    # Create threadpool with mocked pid
    threadpool = ThreadedResolver._create_threadpool(5)
    
    # Assertions to verify a new threadpool is created and pid is updated
    assert ThreadedResolver._threadpool is not None
    assert ThreadedResolver._threadpool_pid == 67890
    assert isinstance(threadpool, concurrent.futures.ThreadPoolExecutor)
    assert threadpool != old_threadpool
