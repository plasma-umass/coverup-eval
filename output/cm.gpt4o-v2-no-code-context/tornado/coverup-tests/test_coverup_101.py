# file: tornado/httpclient.py:551-556
# asked: {"lines": [551, 552, 556], "branches": []}
# gained: {"lines": [551, 552, 556], "branches": []}

import pytest
from tornado import httputil
from tornado.httpclient import HTTPRequest

class TestHTTPRequest:
    def test_headers_property(self, monkeypatch):
        # Create a mock HTTPHeaders object
        mock_headers = httputil.HTTPHeaders({"Content-Type": "application/json"})
        
        # Create an instance of HTTPRequest
        request = HTTPRequest(url="http://example.com")
        
        # Use monkeypatch to set the _headers attribute directly
        monkeypatch.setattr(request, "_headers", mock_headers)
        
        # Access the headers property and assert it returns the mock_headers
        assert request.headers == mock_headers
