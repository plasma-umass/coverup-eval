# file tornado/tcpclient.py:205-211
# lines [205, 206, 207, 208, 210, 211]
# branches ['206->207', '206->210']

import pytest
from tornado.tcpclient import TCPClient
from tornado.netutil import Resolver

@pytest.fixture
def mock_resolver(mocker):
    return mocker.Mock(spec=Resolver)

@pytest.fixture
def tcp_client_with_default_resolver():
    client = TCPClient()
    yield client
    if client._own_resolver:
        client.resolver.close()

def test_tcpclient_with_custom_resolver(mock_resolver):
    client = TCPClient(resolver=mock_resolver)
    assert client.resolver == mock_resolver
    assert not client._own_resolver

def test_tcpclient_with_default_resolver(tcp_client_with_default_resolver):
    client = tcp_client_with_default_resolver
    assert isinstance(client.resolver, Resolver)
    assert client._own_resolver
