# file tornado/netutil.py:462-502
# lines [487, 488]
# branches []

import os
import pytest
from concurrent.futures import ThreadPoolExecutor
from tornado.netutil import ThreadedResolver

@pytest.fixture
def mock_threadpool(mocker):
    mock_pool = mocker.MagicMock(spec=ThreadPoolExecutor)
    mocker.patch.object(ThreadedResolver, '_threadpool', new=mock_pool)
    mocker.patch.object(ThreadedResolver, '_threadpool_pid', new=os.getpid())
    return mock_pool

def test_threaded_resolver_initialize_calls_create_threadpool(mock_threadpool):
    resolver = ThreadedResolver()
    num_threads = 5
    resolver.initialize(num_threads=num_threads)
    assert ThreadedResolver._threadpool is mock_threadpool
    assert ThreadedResolver._threadpool_pid == os.getpid()
    mock_threadpool.shutdown.assert_not_called()
