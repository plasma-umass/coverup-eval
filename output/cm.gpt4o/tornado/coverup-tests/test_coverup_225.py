# file tornado/simple_httpclient.py:89-157
# lines [148, 149, 154, 155]
# branches ['147->148', '153->154']

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest, HTTPResponse
from tornado.ioloop import IOLoop
from tornado.netutil import Resolver, OverrideResolver
from unittest.mock import Mock

@pytest.fixture
def mock_resolver(mocker):
    return mocker.Mock(spec=Resolver)

@pytest.fixture
def mock_override_resolver(mocker):
    return mocker.Mock(spec=OverrideResolver)

def test_simple_async_http_client_with_resolver(mock_resolver):
    client = SimpleAsyncHTTPClient()
    client.initialize(resolver=mock_resolver)
    assert client.resolver == mock_resolver
    assert client.own_resolver is False

def test_simple_async_http_client_with_hostname_mapping(mock_resolver, mock_override_resolver, mocker):
    mocker.patch('tornado.simple_httpclient.OverrideResolver', return_value=mock_override_resolver)
    hostname_mapping = {'example.com': '127.0.0.1'}
    client = SimpleAsyncHTTPClient()
    client.initialize(resolver=mock_resolver, hostname_mapping=hostname_mapping)
    assert client.resolver == mock_override_resolver
    assert client.own_resolver is False

@pytest.fixture
def cleanup():
    yield
    IOLoop.clear_current()

def test_simple_async_http_client_cleanup(cleanup):
    client = SimpleAsyncHTTPClient()
    assert client is not None
