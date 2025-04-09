# file: tornado/netutil.py:339-363
# asked: {"lines": [363], "branches": []}
# gained: {"lines": [363], "branches": []}

import pytest
import socket
from tornado.netutil import Resolver
from typing import List, Any, Tuple, Awaitable

class TestResolver(Resolver):
    def resolve(self, host: str, port: int, family: socket.AddressFamily = socket.AF_UNSPEC) -> Awaitable[List[Tuple[int, Any]]]:
        return super().resolve(host, port, family)

def test_resolver_not_implemented():
    resolver = TestResolver()
    with pytest.raises(NotImplementedError):
        resolver.resolve("localhost", 80)
