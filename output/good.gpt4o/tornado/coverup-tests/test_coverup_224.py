# file tornado/httpclient.py:216-221
# lines [220]
# branches ['219->220']

import pytest
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop

@pytest.fixture
def mock_ioloop(mocker):
    mock_loop = mocker.patch.object(IOLoop, 'current', return_value=mocker.Mock())
    return mock_loop

def test_async_http_client_initialize_with_defaults(mock_ioloop):
    defaults = {'key': 'value'}
    client = AsyncHTTPClient()
    client.initialize(defaults=defaults)
    
    assert client.defaults['key'] == 'value'
    assert client._closed is False

def test_async_http_client_initialize_without_defaults(mock_ioloop):
    client = AsyncHTTPClient()
    client.initialize()
    
    assert 'key' not in client.defaults
    assert client._closed is False
