# file tornado/httpclient.py:216-221
# lines [216, 217, 218, 219, 220, 221]
# branches ['219->220', '219->221']

import pytest
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.ioloop import IOLoop

@pytest.fixture
def mock_ioloop(mocker):
    mock_loop = mocker.Mock(spec=IOLoop)
    mocker.patch('tornado.ioloop.IOLoop.current', return_value=mock_loop)
    return mock_loop

def test_async_http_client_initialize_with_defaults(mock_ioloop):
    defaults = {'method': 'GET'}
    client = AsyncHTTPClient()
    client.initialize(defaults=defaults)

    assert client.io_loop is mock_ioloop
    assert client.defaults['method'] == 'GET'
    assert client._closed is False

def test_async_http_client_initialize_without_defaults(mock_ioloop):
    client = AsyncHTTPClient()
    client.initialize()

    assert client.io_loop is mock_ioloop
    assert client.defaults == HTTPRequest._DEFAULTS
    assert client._closed is False
