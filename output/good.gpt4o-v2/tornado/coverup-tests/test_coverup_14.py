# file: tornado/netutil.py:404-444
# asked: {"lines": [404, 405, 422, 424, 425, 427, 428, 429, 430, 432, 433, 435, 436, 437, 438, 440, 441, 442, 444], "branches": [[428, 429], [428, 432], [436, 437], [436, 438]]}
# gained: {"lines": [404, 405, 422, 424, 425, 427, 428, 429, 430, 432, 433, 435, 436, 437, 438, 440, 441, 442], "branches": [[428, 429], [428, 432], [436, 437], [436, 438]]}

import pytest
import concurrent.futures
import socket
from tornado.netutil import ExecutorResolver
from tornado.ioloop import IOLoop
from tornado.concurrent import dummy_executor

@pytest.fixture
def resolver():
    resolver = ExecutorResolver()
    yield resolver
    if resolver.executor is not None:
        resolver.close()

def test_executor_resolver_with_custom_executor(resolver):
    custom_executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    resolver.initialize(executor=custom_executor, close_executor=True)
    assert resolver.executor == custom_executor
    assert resolver.close_executor is True

def test_executor_resolver_with_dummy_executor(resolver):
    resolver.initialize()
    assert resolver.executor == dummy_executor
    assert resolver.close_executor is False

def test_executor_resolver_close_with_custom_executor(resolver):
    custom_executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    resolver.initialize(executor=custom_executor, close_executor=True)
    resolver.close()
    assert resolver.executor is None

def test_executor_resolver_close_with_dummy_executor(resolver):
    resolver.initialize()
    resolver.close()
    assert resolver.executor is None

@pytest.mark.asyncio
async def test_executor_resolver_resolve(monkeypatch):
    async def mock_resolve_addr(host, port, family):
        return [(socket.AF_INET, ('127.0.0.1', port))]

    monkeypatch.setattr('tornado.netutil._resolve_addr', mock_resolve_addr)

    resolver = ExecutorResolver()
    resolver.initialize()
    result = await resolver.resolve('localhost', 80)
    assert result == [(socket.AF_INET, ('127.0.0.1', 80))]
    resolver.close()
