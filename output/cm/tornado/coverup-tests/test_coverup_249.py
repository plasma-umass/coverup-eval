# file tornado/httpclient.py:309-312
# lines [312]
# branches []

import pytest
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from typing import Callable

class TestAsyncHTTPClient(AsyncHTTPClient):
    def fetch_impl(self, request: "HTTPRequest", callback: Callable[["HTTPResponse"], None]) -> None:
        super().fetch_impl(request, callback)

def test_async_http_client_fetch_impl():
    client = TestAsyncHTTPClient()
    with pytest.raises(NotImplementedError):
        client.fetch_impl(HTTPRequest(url='http://example.com'), lambda response: None)
