# file tornado/httpclient.py:309-312
# lines [309, 312]
# branches []

import pytest
from typing import Callable
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPResponse

class CustomAsyncHTTPClient(AsyncHTTPClient):
    def fetch_impl(
        self, request: HTTPRequest, callback: Callable[[HTTPResponse], None]
    ) -> None:
        super().fetch_impl(request, callback)

def test_fetch_impl_not_implemented():
    client = CustomAsyncHTTPClient()
    request = HTTPRequest(url="http://example.com", connect_timeout=10)
    
    with pytest.raises(NotImplementedError):
        client.fetch_impl(request, lambda response: None)
