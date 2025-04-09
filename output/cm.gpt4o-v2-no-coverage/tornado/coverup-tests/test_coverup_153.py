# file: tornado/httpclient.py:309-312
# asked: {"lines": [309, 312], "branches": []}
# gained: {"lines": [309, 312], "branches": []}

import pytest
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPResponse
from tornado.util import Configurable

class TestAsyncHTTPClient:
    def test_fetch_impl_not_implemented(self, monkeypatch):
        class MockAsyncHTTPClient(AsyncHTTPClient):
            def fetch_impl(self, request, callback):
                super().fetch_impl(request, callback)
        
        client = MockAsyncHTTPClient()
        request = HTTPRequest(url="http://example.com", connect_timeout=10)
        
        with pytest.raises(NotImplementedError):
            client.fetch_impl(request, lambda response: None)
