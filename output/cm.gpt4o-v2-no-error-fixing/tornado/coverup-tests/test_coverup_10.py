# file: tornado/netutil.py:404-444
# asked: {"lines": [404, 405, 422, 424, 425, 427, 428, 429, 430, 432, 433, 435, 436, 437, 438, 440, 441, 442, 444], "branches": [[428, 429], [428, 432], [436, 437], [436, 438]]}
# gained: {"lines": [404, 405, 422, 424, 425, 427, 428, 429, 430, 432, 433, 435, 436, 437, 438, 440, 441, 442, 444], "branches": [[428, 429], [428, 432], [436, 437], [436, 438]]}

import pytest
import concurrent.futures
import socket
from tornado.ioloop import IOLoop
from tornado.netutil import ExecutorResolver
from unittest.mock import patch

@pytest.fixture
def resolver():
    return ExecutorResolver()

def test_initialize_with_executor(resolver):
    executor = concurrent.futures.ThreadPoolExecutor()
    resolver.initialize(executor=executor, close_executor=True)
    assert resolver.executor == executor
    assert resolver.close_executor is True

def test_initialize_without_executor(resolver):
    resolver.initialize()
    assert resolver.executor is not None
    assert resolver.close_executor is False

def test_close_with_executor(resolver):
    executor = concurrent.futures.ThreadPoolExecutor()
    resolver.initialize(executor=executor, close_executor=True)
    resolver.close()
    assert resolver.executor is None

def test_close_without_executor(resolver):
    resolver.initialize()
    resolver.close()
    assert resolver.executor is None

@patch('tornado.netutil._resolve_addr', return_value=[(socket.AF_INET, ('127.0.0.1', 80))])
def test_resolve(mock_resolve_addr, resolver):
    resolver.initialize()
    result = IOLoop.current().run_sync(lambda: resolver.resolve('localhost', 80))
    assert result == [(socket.AF_INET, ('127.0.0.1', 80))]
    mock_resolve_addr.assert_called_once_with('localhost', 80, socket.AF_UNSPEC)
