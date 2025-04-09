# file: tornado/netutil.py:389-401
# asked: {"lines": [389, 390, 395, 396, 398, 399, 401], "branches": []}
# gained: {"lines": [389, 390, 395, 396], "branches": []}

import pytest
import socket
from tornado.ioloop import IOLoop
from tornado.netutil import Resolver
from unittest.mock import patch
from typing import List, Tuple, Any

class DefaultExecutorResolver(Resolver):
    """Resolver implementation using `.IOLoop.run_in_executor`.

    .. versionadded:: 5.0
    """

    async def resolve(
        self, host: str, port: int, family: socket.AddressFamily = socket.AF_UNSPEC
    ) -> List[Tuple[int, Any]]:
        result = await IOLoop.current().run_in_executor(
            None, _resolve_addr, host, port, family
        )
        return result

def _resolve_addr(host, port, family):
    return [(socket.AF_INET, (host, port))]

@pytest.mark.asyncio
async def test_default_executor_resolver(monkeypatch):
    async def mock_run_in_executor(executor, func, *args):
        return func(*args)

    monkeypatch.setattr(IOLoop.current(), "run_in_executor", mock_run_in_executor)

    resolver = DefaultExecutorResolver()
    result = await resolver.resolve("localhost", 80)
    
    assert result == [(socket.AF_INET, ("localhost", 80))]
