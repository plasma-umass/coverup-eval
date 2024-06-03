# file tornado/netutil.py:389-401
# lines [389, 390, 395, 396, 398, 399, 401]
# branches []

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
async def test_default_executor_resolver(mocker):
    resolver = DefaultExecutorResolver()
    host = 'localhost'
    port = 80
    family = socket.AF_INET

    mocker.patch('tornado.ioloop.IOLoop.current', return_value=IOLoop.instance())
    mocker.patch('tornado.ioloop.IOLoop.run_in_executor', return_value=[(family, (host, port))])

    result = await resolver.resolve(host, port, family)
    
    assert result == [(family, (host, port))]
