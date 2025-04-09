# file tornado/netutil.py:505-544
# lines [505, 506, 528, 529, 530, 532, 533, 535, 536, 538, 539, 540, 541, 542, 543, 544]
# branches ['538->539', '538->540', '540->541', '540->542', '542->543', '542->544']

import socket
from tornado.netutil import Resolver, OverrideResolver
import pytest
from unittest.mock import AsyncMock

@pytest.fixture
def mock_resolver():
    resolver = AsyncMock(spec=Resolver)
    resolver.resolve.return_value = [("resolved", 1234)]
    return resolver

@pytest.mark.asyncio
async def test_override_resolver(mock_resolver):
    mapping = {
        "example.com": "127.0.1.1",
        ("login.example.com", 443): ("localhost", 1443),
        ("login.example.com", 443, socket.AF_INET6): ("::1", 1443),
    }
    override_resolver = OverrideResolver(resolver=mock_resolver, mapping=mapping)

    # Test hostname override
    result = await override_resolver.resolve("example.com", 80)
    mock_resolver.resolve.assert_called_once_with("127.0.1.1", 80, socket.AF_UNSPEC)
    assert result == [("resolved", 1234)]
    mock_resolver.resolve.reset_mock()

    # Test host+port override
    result = await override_resolver.resolve("login.example.com", 443)
    mock_resolver.resolve.assert_called_once_with("localhost", 1443, socket.AF_UNSPEC)
    assert result == [("resolved", 1234)]
    mock_resolver.resolve.reset_mock()

    # Test host+port+family override
    result = await override_resolver.resolve("login.example.com", 443, socket.AF_INET6)
    mock_resolver.resolve.assert_called_once_with("::1", 1443, socket.AF_INET6)
    assert result == [("resolved", 1234)]
    mock_resolver.resolve.reset_mock()

    # Test no override
    result = await override_resolver.resolve("no-override.com", 80)
    mock_resolver.resolve.assert_called_once_with("no-override.com", 80, socket.AF_UNSPEC)
    assert result == [("resolved", 1234)]
    mock_resolver.resolve.reset_mock()

    # Clean up
    override_resolver.close()
