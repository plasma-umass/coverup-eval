# file tornado/netutil.py:339-363
# lines [339, 340, 363]
# branches []

import pytest
import socket
from tornado.netutil import Resolver

class TestResolver(Resolver):
    def resolve(self, host, port, family=socket.AF_UNSPEC):
        return super().resolve(host, port, family)

@pytest.fixture
def mock_resolver(mocker):
    return mocker.patch('tornado.netutil.Resolver', TestResolver)

def test_resolver_resolve_not_implemented_error(mock_resolver):
    resolver = Resolver()
    with pytest.raises(NotImplementedError):
        result = resolver.resolve('localhost', 80)
        pytest.assume(isinstance(result, Awaitable))
