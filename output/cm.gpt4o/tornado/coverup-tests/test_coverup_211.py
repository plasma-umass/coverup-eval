# file tornado/netutil.py:505-544
# lines [529, 530, 533, 538, 539, 540, 541, 542, 543, 544]
# branches ['538->539', '538->540', '540->541', '540->542', '542->543', '542->544']

import pytest
import socket
from tornado.netutil import Resolver

class MockResolver(Resolver):
    def close(self):
        pass

    async def resolve(self, host, port, family=socket.AF_UNSPEC):
        return [(family, (host, port))]

@pytest.fixture
def override_resolver():
    from tornado.netutil import OverrideResolver
    resolver = MockResolver()
    mapping = {
        "example.com": "127.0.1.1",
        ("login.example.com", 443): ("localhost", 1443),
        ("login.example.com", 443, socket.AF_INET6): ("::1", 1443),
    }
    override_resolver = OverrideResolver(resolver, mapping)
    yield override_resolver
    override_resolver.close()

@pytest.mark.asyncio
async def test_override_resolver(override_resolver):
    # Test host+port+family mapping
    result = await override_resolver.resolve("login.example.com", 443, socket.AF_INET6)
    assert result == [(socket.AF_INET6, ("::1", 1443))]

    # Test host+port mapping
    result = await override_resolver.resolve("login.example.com", 443)
    assert result == [(socket.AF_UNSPEC, ("localhost", 1443))]

    # Test host mapping
    result = await override_resolver.resolve("example.com", 80)
    assert result == [(socket.AF_UNSPEC, ("127.0.1.1", 80))]

    # Test no mapping
    result = await override_resolver.resolve("no-mapping.com", 80)
    assert result == [(socket.AF_UNSPEC, ("no-mapping.com", 80))]
