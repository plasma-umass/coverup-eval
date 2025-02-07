# file: tornado/netutil.py:505-544
# asked: {"lines": [505, 506, 528, 529, 530, 532, 533, 535, 536, 538, 539, 540, 541, 542, 543, 544], "branches": [[538, 539], [538, 540], [540, 541], [540, 542], [542, 543], [542, 544]]}
# gained: {"lines": [505, 506, 528, 529, 530, 532, 533, 535, 536], "branches": []}

import pytest
import socket
from unittest.mock import MagicMock
from tornado.netutil import Resolver, OverrideResolver

class TestOverrideResolver:
    
    @pytest.fixture
    def setup_resolver(self):
        resolver = MagicMock(spec=Resolver)
        mapping = {
            "example.com": "127.0.1.1",
            ("login.example.com", 443): ("localhost", 1443),
            ("login.example.com", 443, socket.AF_INET6): ("::1", 1443),
        }
        override_resolver = OverrideResolver(resolver, mapping)
        return override_resolver, resolver

    def test_initialize(self, setup_resolver):
        override_resolver, resolver = setup_resolver
        assert override_resolver.resolver == resolver
        assert override_resolver.mapping == {
            "example.com": "127.0.1.1",
            ("login.example.com", 443): ("localhost", 1443),
            ("login.example.com", 443, socket.AF_INET6): ("::1", 1443),
        }

    def test_close(self, setup_resolver):
        override_resolver, resolver = setup_resolver
        override_resolver.close()
        resolver.close.assert_called_once()

    @pytest.mark.asyncio
    async def test_resolve_host_port_family(self, setup_resolver):
        override_resolver, resolver = setup_resolver
        await override_resolver.resolve("login.example.com", 443, socket.AF_INET6)
        resolver.resolve.assert_called_once_with("::1", 1443, socket.AF_INET6)

    @pytest.mark.asyncio
    async def test_resolve_host_port(self, setup_resolver):
        override_resolver, resolver = setup_resolver
        await override_resolver.resolve("login.example.com", 443)
        resolver.resolve.assert_called_once_with("localhost", 1443, socket.AF_UNSPEC)

    @pytest.mark.asyncio
    async def test_resolve_host(self, setup_resolver):
        override_resolver, resolver = setup_resolver
        await override_resolver.resolve("example.com", 80)
        resolver.resolve.assert_called_once_with("127.0.1.1", 80, socket.AF_UNSPEC)

    @pytest.mark.asyncio
    async def test_resolve_no_override(self, setup_resolver):
        override_resolver, resolver = setup_resolver
        await override_resolver.resolve("no-override.com", 80)
        resolver.resolve.assert_called_once_with("no-override.com", 80, socket.AF_UNSPEC)
