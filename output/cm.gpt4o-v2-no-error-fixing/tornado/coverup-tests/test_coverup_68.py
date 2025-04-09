# file: tornado/netutil.py:389-401
# asked: {"lines": [389, 390, 395, 396, 398, 399, 401], "branches": []}
# gained: {"lines": [389, 390, 395, 396], "branches": []}

import pytest
import socket
from tornado.ioloop import IOLoop
from tornado.netutil import DefaultExecutorResolver

@pytest.mark.asyncio
async def test_resolve(monkeypatch):
    async def mock_run_in_executor(self, executor, func, *args):
        return await func(*args)

    monkeypatch.setattr(IOLoop, 'run_in_executor', mock_run_in_executor)

    resolver = DefaultExecutorResolver()
    result = await resolver.resolve('localhost', 80, socket.AF_INET)
    
    assert isinstance(result, list)
    assert all(isinstance(item, tuple) and len(item) == 2 for item in result)
    assert all(isinstance(item[0], int) and isinstance(item[1], tuple) for item in result)
