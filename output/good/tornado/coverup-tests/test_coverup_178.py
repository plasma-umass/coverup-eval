# file tornado/simple_httpclient.py:202-203
# lines [202, 203]
# branches []

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest
from unittest.mock import patch

@pytest.fixture
def mock_http_connection():
    with patch('tornado.simple_httpclient._HTTPConnection') as mock:
        yield mock

@pytest.mark.gen_test
async def test_connection_class(mock_http_connection):
    client = SimpleAsyncHTTPClient()
    request = HTTPRequest(url='http://example.com')
    connection = client.fetch(request)
    assert mock_http_connection.called
    # Clean up the client after the test
    client.close()
