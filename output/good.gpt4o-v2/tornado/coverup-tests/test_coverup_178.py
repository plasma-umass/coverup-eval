# file: tornado/netutil.py:339-363
# asked: {"lines": [339, 340, 363], "branches": []}
# gained: {"lines": [339, 340, 363], "branches": []}

import pytest
import socket
from tornado.netutil import Resolver
from tornado.concurrent import Future
from typing import Awaitable, List, Tuple, Any

class TestResolver(Resolver):
    def resolve(self, host: str, port: int, family: socket.AddressFamily = socket.AF_UNSPEC) -> Awaitable[List[Tuple[int, Any]]]:
        future = Future()
        future.set_result([(family, (host, port))])
        return future

def test_resolver_resolve():
    resolver = TestResolver()
    host = 'localhost'
    port = 80
    family = socket.AF_INET

    future = resolver.resolve(host, port, family)
    result = future.result()

    assert len(result) == 1
    assert result[0] == (family, (host, port))

def test_resolver_not_implemented():
    class IncompleteResolver(Resolver):
        pass

    resolver = IncompleteResolver()
    with pytest.raises(NotImplementedError):
        resolver.resolve('localhost', 80)
