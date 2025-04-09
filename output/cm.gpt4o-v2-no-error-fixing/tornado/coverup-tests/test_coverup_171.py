# file: tornado/netutil.py:505-544
# asked: {"lines": [529, 530, 533, 538, 539, 540, 541, 542, 543, 544], "branches": [[538, 539], [538, 540], [540, 541], [540, 542], [542, 543], [542, 544]]}
# gained: {"lines": [529, 530, 533], "branches": []}

import pytest
import socket
from unittest import mock
from tornado.netutil import Resolver, OverrideResolver

class FakeResolver(Resolver):
    async def resolve(self, host, port, family=socket.AF_UNSPEC):
        return [(family, (host, port))]

    def close(self):
        pass

@pytest.fixture
def fake_resolver():
    return FakeResolver()

@pytest.fixture
def override_resolver(fake_resolver):
    return OverrideResolver(resolver=fake_resolver, mapping={})

def test_initialize(override_resolver, fake_resolver):
    resolver = override_resolver
    resolver.initialize(fake_resolver, {"example.com": "127.0.0.1"})
    assert resolver.resolver == fake_resolver
    assert resolver.mapping == {"example.com": "127.0.0.1"}

def test_close(override_resolver, fake_resolver):
    resolver = override_resolver
    with mock.patch.object(fake_resolver, 'close') as mock_close:
        resolver.close()
        mock_close.assert_called_once()

@pytest.mark.asyncio
async def test_resolve_host_port_family(override_resolver):
    resolver = override_resolver
    resolver.initialize(resolver.resolver, {("example.com", 80, socket.AF_INET): ("127.0.0.1", 8080)})
    result = await resolver.resolve("example.com", 80, socket.AF_INET)
    assert result == [(socket.AF_INET, ("127.0.0.1", 8080))]

@pytest.mark.asyncio
async def test_resolve_host_port(override_resolver):
    resolver = override_resolver
    resolver.initialize(resolver.resolver, {("example.com", 80): ("127.0.0.1", 8080)})
    result = await resolver.resolve("example.com", 80)
    assert result == [(socket.AF_UNSPEC, ("127.0.0.1", 8080))]

@pytest.mark.asyncio
async def test_resolve_host(override_resolver):
    resolver = override_resolver
    resolver.initialize(resolver.resolver, {"example.com": "127.0.0.1"})
    result = await resolver.resolve("example.com", 80)
    assert result == [(socket.AF_UNSPEC, ("127.0.0.1", 80))]
