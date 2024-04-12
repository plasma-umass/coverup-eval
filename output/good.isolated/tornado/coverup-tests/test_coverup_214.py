# file tornado/netutil.py:404-444
# lines [427, 428, 429, 430, 432, 433, 436, 437, 438, 444]
# branches ['428->429', '428->432', '436->437', '436->438']

import pytest
from unittest.mock import Mock
from tornado.netutil import ExecutorResolver
from tornado.ioloop import IOLoop
from concurrent.futures import ThreadPoolExecutor

@pytest.fixture
def mock_executor():
    executor = Mock(spec=ThreadPoolExecutor)
    executor.shutdown = Mock()
    return executor

@pytest.fixture
def io_loop():
    loop = IOLoop()
    loop.make_current()
    yield loop
    loop.clear_current()
    loop.close(all_fds=True)

def test_executor_resolver_with_custom_executor(mock_executor, io_loop):
    resolver = ExecutorResolver(executor=mock_executor, close_executor=True)
    assert resolver.executor is mock_executor
    assert resolver.close_executor is True

    resolver.close()
    mock_executor.shutdown.assert_called_once()

def test_executor_resolver_with_dummy_executor(io_loop):
    resolver = ExecutorResolver()
    assert resolver.executor is not None
    assert resolver.close_executor is False

    resolver.close()
    assert resolver.executor is None

# Removed the test_resolve_method as it was incorrect and not necessary for coverage
