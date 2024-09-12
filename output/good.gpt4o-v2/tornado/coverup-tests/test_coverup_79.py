# file: tornado/netutil.py:389-401
# asked: {"lines": [389, 390, 395, 396, 398, 399, 401], "branches": []}
# gained: {"lines": [389, 390, 395, 396], "branches": []}

import pytest
import socket
from tornado.ioloop import IOLoop
from tornado.netutil import DefaultExecutorResolver

@pytest.mark.asyncio
async def test_default_executor_resolver(monkeypatch):
    async def mock_run_in_executor(executor, func, *args):
        return [(socket.AF_INET, ('127.0.0.1', 80))]

    monkeypatch.setattr(IOLoop.current(), 'run_in_executor', mock_run_in_executor)

    resolver = DefaultExecutorResolver()
    result = await resolver.resolve('localhost', 80)
    
    assert result == [(socket.AF_INET, ('127.0.0.1', 80))]

    resolver.close()
