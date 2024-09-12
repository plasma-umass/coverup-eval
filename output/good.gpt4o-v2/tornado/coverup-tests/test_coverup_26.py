# file: tornado/netutil.py:462-502
# asked: {"lines": [462, 463, 483, 484, 486, 487, 488, 490, 491, 494, 495, 498, 499, 500, 501, 502], "branches": [[495, 498], [495, 499], [499, 500], [499, 502]]}
# gained: {"lines": [462, 463, 483, 484, 486, 487, 488, 490, 491, 494, 495, 498, 499, 500, 501, 502], "branches": [[495, 498], [499, 500]]}

import pytest
import os
from tornado.netutil import ThreadedResolver

def test_threaded_resolver_initialize(mocker):
    mock_threadpool = mocker.patch('tornado.netutil.ThreadedResolver._create_threadpool')
    resolver = ThreadedResolver()
    
    # Ensure the threadpool is None initially
    ThreadedResolver._threadpool = None
    ThreadedResolver._threadpool_pid = None
    
    resolver.initialize(num_threads=5)
    mock_threadpool.assert_any_call(5)

def test_threaded_resolver_create_threadpool(mocker):
    mock_threadpool_executor = mocker.patch('concurrent.futures.ThreadPoolExecutor')
    mock_pid = mocker.patch('os.getpid', return_value=12345)
    
    # Ensure the threadpool is None initially
    ThreadedResolver._threadpool = None
    ThreadedResolver._threadpool_pid = None
    
    # First call to _create_threadpool
    pool = ThreadedResolver._create_threadpool(5)
    mock_threadpool_executor.assert_called_once_with(5)
    assert ThreadedResolver._threadpool is pool
    assert ThreadedResolver._threadpool_pid == 12345
    
    # Simulate a fork by changing the PID
    mock_pid.return_value = 54321
    
    # Second call to _create_threadpool should detect PID change and recreate the pool
    pool = ThreadedResolver._create_threadpool(10)
    assert mock_threadpool_executor.call_count == 2
    assert ThreadedResolver._threadpool is pool
    assert ThreadedResolver._threadpool_pid == 54321
