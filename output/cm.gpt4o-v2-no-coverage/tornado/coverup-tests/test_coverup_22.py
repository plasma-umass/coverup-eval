# file: tornado/netutil.py:404-444
# asked: {"lines": [404, 405, 422, 424, 425, 427, 428, 429, 430, 432, 433, 435, 436, 437, 438, 440, 441, 442, 444], "branches": [[428, 429], [428, 432], [436, 437], [436, 438]]}
# gained: {"lines": [404, 405, 422, 424, 425, 427, 428, 429, 430, 432, 433, 435, 436, 437, 438, 440, 441, 442], "branches": [[428, 429], [428, 432], [436, 437], [436, 438]]}

import pytest
from unittest import mock
from tornado.netutil import ExecutorResolver
from tornado.concurrent import dummy_executor
from tornado.ioloop import IOLoop
import socket
import concurrent.futures

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
    assert resolver.executor == dummy_executor
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

@pytest.mark.asyncio
async def test_resolve(monkeypatch, resolver):
    async def mock_resolve_addr(host, port, family):
        return [(socket.AF_INET, ('127.0.0.1', port))]

    monkeypatch.setattr('tornado.netutil._resolve_addr', mock_resolve_addr)
    resolver.initialize()
    result = await resolver.resolve('localhost', 80)
    assert result == [(socket.AF_INET, ('127.0.0.1', 80))]

@pytest.mark.asyncio
async def test_resolve_with_executor(monkeypatch, resolver):
    async def mock_resolve_addr(host, port, family):
        return [(socket.AF_INET, ('127.0.0.1', port))]

    monkeypatch.setattr('tornado.netutil._resolve_addr', mock_resolve_addr)
    executor = concurrent.futures.ThreadPoolExecutor()
    resolver.initialize(executor=executor, close_executor=True)
    result = await resolver.resolve('localhost', 80)
    assert result == [(socket.AF_INET, ('127.0.0.1', 80))]
    resolver.close()
