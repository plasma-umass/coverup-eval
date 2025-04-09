# file: tornado/httpclient.py:309-312
# asked: {"lines": [309, 312], "branches": []}
# gained: {"lines": [309], "branches": []}

import pytest
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPResponse
from typing import Callable

class CustomAsyncHTTPClient(AsyncHTTPClient):
    def fetch_impl(self, request: HTTPRequest, callback: Callable[[HTTPResponse], None]) -> None:
        raise NotImplementedError()

class TestAsyncHTTPClient:
    def test_fetch_impl_not_implemented(self):
        client = CustomAsyncHTTPClient()
        request = HTTPRequest(url="http://example.com")
        
        with pytest.raises(NotImplementedError):
            client.fetch_impl(request, lambda response: None)
