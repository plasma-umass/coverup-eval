# file tornado/httpclient.py:551-556
# lines [551, 552, 556]
# branches []

import pytest
from tornado.httpclient import HTTPRequest
from tornado import httputil

@pytest.fixture
def http_request():
    request = HTTPRequest(url='http://example.com')
    request._headers = httputil.HTTPHeaders()  # Set the headers to an HTTPHeaders instance
    return request

def test_http_request_headers_property(http_request):
    # Ensure that the headers property returns an instance of HTTPHeaders
    assert isinstance(http_request.headers, httputil.HTTPHeaders), "headers property should return an instance of HTTPHeaders"
