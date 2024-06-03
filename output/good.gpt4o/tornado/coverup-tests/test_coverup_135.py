# file tornado/simple_httpclient.py:255-259
# lines [255, 256, 257]
# branches []

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httputil import HTTPHeaders
from tornado.httpclient import HTTPRequest
from unittest.mock import patch

@pytest.mark.asyncio
async def test_http_connection_methods():
    with patch('tornado.simple_httpclient.SimpleAsyncHTTPClient.fetch_impl') as mock_fetch:
        client = SimpleAsyncHTTPClient()
        url = 'http://example.com'
        
        for method in ["GET", "HEAD", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"]:
            request = HTTPRequest(url, method=method)
            await client.fetch(request)
            assert mock_fetch.called
            called_request = mock_fetch.call_args[0][0]
            assert called_request.method == method
            mock_fetch.reset_mock()
