# file: tornado/netutil.py:505-544
# asked: {"lines": [505, 506, 528, 529, 530, 532, 533, 535, 536, 538, 539, 540, 541, 542, 543, 544], "branches": [[538, 539], [538, 540], [540, 541], [540, 542], [542, 543], [542, 544]]}
# gained: {"lines": [505, 506, 528, 529, 530, 532, 533, 535, 536], "branches": []}

import pytest
import socket
from tornado.netutil import Resolver, OverrideResolver
from unittest.mock import AsyncMock

class MockResolver(Resolver):
    async def resolve(self, host, port, family=socket.AF_UNSPEC):
        return [(family, (host, port))]

@pytest.fixture
def mock_resolver():
    return MockResolver()

@pytest.fixture
def override_resolver(mock_resolver):
    return OverrideResolver(resolver=mock_resolver, mapping={})

@pytest.mark.asyncio
async def test_override_resolver_host_port_family(override_resolver):
    override_resolver.mapping = {("example.com", 80, socket.AF_INET): ("localhost", 8080)}
    result = await override_resolver.resolve("example.com", 80, socket.AF_INET)
    assert result == [(socket.AF_INET, ("localhost", 8080))]

@pytest.mark.asyncio
async def test_override_resolver_host_port(override_resolver):
    override_resolver.mapping = {("example.com", 80): ("localhost", 8080)}
    result = await override_resolver.resolve("example.com", 80)
    assert result == [(socket.AF_UNSPEC, ("localhost", 8080))]

@pytest.mark.asyncio
async def test_override_resolver_host(override_resolver):
    override_resolver.mapping = {"example.com": "localhost"}
    result = await override_resolver.resolve("example.com", 80)
    assert result == [(socket.AF_UNSPEC, ("localhost", 80))]

@pytest.mark.asyncio
async def test_override_resolver_no_override(override_resolver):
    result = await override_resolver.resolve("example.com", 80)
    assert result == [(socket.AF_UNSPEC, ("example.com", 80))]

def test_override_resolver_close(override_resolver, mocker):
    mock_close = mocker.patch.object(override_resolver.resolver, 'close', autospec=True)
    override_resolver.close()
    mock_close.assert_called_once()
