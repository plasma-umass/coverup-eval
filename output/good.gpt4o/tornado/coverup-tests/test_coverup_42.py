# file tornado/netutil.py:505-544
# lines [505, 506, 528, 529, 530, 532, 533, 535, 536, 538, 539, 540, 541, 542, 543, 544]
# branches ['538->539', '538->540', '540->541', '540->542', '542->543', '542->544']

import pytest
import socket
from tornado.netutil import Resolver
from tornado.ioloop import IOLoop
from tornado.testing import AsyncTestCase, gen_test

class MockResolver(Resolver):
    def initialize(self):
        pass

    def close(self):
        pass

    async def resolve(self, host, port, family=socket.AF_UNSPEC):
        return [(family, (host, port))]

class OverrideResolver(Resolver):
    """Wraps a resolver with a mapping of overrides.

    This can be used to make local DNS changes (e.g. for testing)
    without modifying system-wide settings.

    The mapping can be in three formats::

        {
            # Hostname to host or ip
            "example.com": "127.0.1.1",

            # Host+port to host+port
            ("login.example.com", 443): ("localhost", 1443),

            # Host+port+address family to host+port
            ("login.example.com", 443, socket.AF_INET6): ("::1", 1443),
        }

    .. versionchanged:: 5.0
       Added support for host-port-family triplets.
    """

    def initialize(self, resolver: Resolver, mapping: dict) -> None:
        self.resolver = resolver
        self.mapping = mapping

    def close(self) -> None:
        self.resolver.close()

    async def resolve(
        self, host: str, port: int, family: socket.AddressFamily = socket.AF_UNSPEC
    ) -> list:
        if (host, port, family) in self.mapping:
            host, port = self.mapping[(host, port, family)]
        elif (host, port) in self.mapping:
            host, port = self.mapping[(host, port)]
        elif host in self.mapping:
            host = self.mapping[host]
        return await self.resolver.resolve(host, port, family)

class TestOverrideResolver(AsyncTestCase):
    @gen_test
    async def test_override_resolver(self):
        mapping = {
            "example.com": "127.0.1.1",
            ("login.example.com", 443): ("localhost", 1443),
            ("login.example.com", 443, socket.AF_INET6): ("::1", 1443),
        }
        resolver = MockResolver()
        override_resolver = OverrideResolver(resolver, mapping)

        # Test host+port+family override
        result = await override_resolver.resolve("login.example.com", 443, socket.AF_INET6)
        assert result == [(socket.AF_INET6, ("::1", 1443))]

        # Test host+port override
        result = await override_resolver.resolve("login.example.com", 443)
        assert result == [(socket.AF_UNSPEC, ("localhost", 1443))]

        # Test host override
        result = await override_resolver.resolve("example.com", 80)
        assert result == [(socket.AF_UNSPEC, ("127.0.1.1", 80))]

        # Test no override
        result = await override_resolver.resolve("no-override.com", 80)
        assert result == [(socket.AF_UNSPEC, ("no-override.com", 80))]

        override_resolver.close()
