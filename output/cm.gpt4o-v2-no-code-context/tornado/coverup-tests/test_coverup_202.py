# file: tornado/netutil.py:404-444
# asked: {"lines": [427, 428, 429, 430, 432, 433, 436, 437, 438, 444], "branches": [[428, 429], [428, 432], [436, 437], [436, 438]]}
# gained: {"lines": [427, 428, 429, 430, 432, 433, 436, 437, 438], "branches": [[428, 429], [428, 432], [436, 437], [436, 438]]}

import pytest
from tornado.netutil import ExecutorResolver
from tornado.ioloop import IOLoop
import concurrent.futures
from unittest import mock
import socket

@pytest.fixture
def dummy_executor():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        yield executor

@pytest.fixture
def resolver():
    return ExecutorResolver()

def test_initialize_with_executor(resolver, dummy_executor):
    resolver.initialize(executor=dummy_executor, close_executor=True)
    assert resolver.executor == dummy_executor
    assert resolver.close_executor is True

def test_initialize_without_executor(resolver, monkeypatch):
    dummy_executor = mock.Mock()
    monkeypatch.setattr('tornado.netutil.dummy_executor', dummy_executor)
    resolver.initialize(executor=None, close_executor=True)
    assert resolver.executor == dummy_executor
    assert resolver.close_executor is False

def test_close_with_executor(resolver, dummy_executor):
    resolver.initialize(executor=dummy_executor, close_executor=True)
    with mock.patch.object(dummy_executor, 'shutdown', wraps=dummy_executor.shutdown) as mock_shutdown:
        resolver.close()
        mock_shutdown.assert_called_once()
    assert resolver.executor is None

def test_close_without_executor_shutdown(resolver, dummy_executor):
    resolver.initialize(executor=dummy_executor, close_executor=False)
    with mock.patch.object(dummy_executor, 'shutdown', wraps=dummy_executor.shutdown) as mock_shutdown:
        resolver.close()
        mock_shutdown.assert_not_called()
    assert resolver.executor is None

@pytest.mark.asyncio
async def test_resolve(resolver, dummy_executor, monkeypatch):
    resolver.initialize(executor=dummy_executor, close_executor=True)
    mock_resolve_addr = mock.Mock(return_value=[(2, '127.0.0.1')])
    monkeypatch.setattr('tornado.netutil._resolve_addr', mock_resolve_addr)
    result = await resolver.resolve('localhost', 80)
    assert result == [(2, '127.0.0.1')]
    mock_resolve_addr.assert_called_once_with('localhost', 80, socket.AF_UNSPEC)
