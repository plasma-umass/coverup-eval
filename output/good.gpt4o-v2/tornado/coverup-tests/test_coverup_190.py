# file: tornado/httpclient.py:309-312
# asked: {"lines": [309, 312], "branches": []}
# gained: {"lines": [309, 312], "branches": []}

import pytest
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.util import Configurable

class TestAsyncHTTPClient(AsyncHTTPClient):
    def fetch_impl(self, request, callback):
        super().fetch_impl(request, callback)

def test_fetch_impl_not_implemented():
    client = TestAsyncHTTPClient()
    request = HTTPRequest(url="http://example.com", connect_timeout=10, request_timeout=10)
    callback = lambda response: None

    with pytest.raises(NotImplementedError):
        client.fetch_impl(request, callback)
