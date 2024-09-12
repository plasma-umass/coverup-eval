# file: tornado/httpclient.py:629-669
# asked: {"lines": [629, 633, 634, 635, 636, 637, 638, 639, 640, 642, 643, 645, 646, 647, 648, 649, 651, 652, 653, 654, 655, 657, 658, 659, 660, 661, 662, 664, 666, 667, 668, 669], "branches": [[642, 643], [642, 645], [648, 649], [648, 651], [654, 655], [654, 657], [659, 660], [659, 666], [660, 661], [660, 664]]}
# gained: {"lines": [629, 633, 634, 635, 636, 637, 638, 639, 640, 642, 645, 646, 647, 648, 649, 651, 652, 653, 654, 655, 657, 658, 659, 660, 661, 662, 664, 666, 667, 668, 669], "branches": [[642, 645], [648, 649], [648, 651], [654, 655], [654, 657], [659, 660], [659, 666], [660, 661], [660, 664]]}

import pytest
from io import BytesIO
from tornado.httpclient import HTTPResponse, HTTPRequest, HTTPError
from tornado.httputil import HTTPHeaders

class MockRequestProxy:
    def __init__(self, request):
        self.request = request

    def __getattr__(self, name):
        return getattr(self.request, name)

@pytest.fixture
def mock_request():
    return HTTPRequest(url="http://example.com")

def test_http_response_init_with_request_proxy(mock_request):
    proxy = MockRequestProxy(mock_request)
    response = HTTPResponse(request=proxy, code=200)
    assert response.request == proxy

def test_http_response_init_with_headers(mock_request):
    headers = HTTPHeaders({"Content-Type": "text/html"})
    response = HTTPResponse(request=mock_request, code=200, headers=headers)
    assert response.headers == headers

def test_http_response_init_without_headers(mock_request):
    response = HTTPResponse(request=mock_request, code=200)
    assert isinstance(response.headers, HTTPHeaders)

def test_http_response_init_with_buffer(mock_request):
    buffer = BytesIO(b"test")
    response = HTTPResponse(request=mock_request, code=200, buffer=buffer)
    assert response.buffer == buffer

def test_http_response_init_with_effective_url(mock_request):
    effective_url = "http://example.org"
    response = HTTPResponse(request=mock_request, code=200, effective_url=effective_url)
    assert response.effective_url == effective_url

def test_http_response_init_without_effective_url(mock_request):
    response = HTTPResponse(request=mock_request, code=200)
    assert response.effective_url == mock_request.url

def test_http_response_init_with_error(mock_request):
    error = HTTPError(500, "Server Error")
    response = HTTPResponse(request=mock_request, code=500, error=error)
    assert response.error == error

def test_http_response_init_without_error(mock_request):
    response = HTTPResponse(request=mock_request, code=500)
    assert isinstance(response.error, HTTPError)
    assert response.error.code == 500

def test_http_response_init_with_request_time(mock_request):
    request_time = 1.23
    response = HTTPResponse(request=mock_request, code=200, request_time=request_time)
    assert response.request_time == request_time

def test_http_response_init_with_time_info(mock_request):
    time_info = {"starttransfer": 0.1}
    response = HTTPResponse(request=mock_request, code=200, time_info=time_info)
    assert response.time_info == time_info

def test_http_response_init_without_time_info(mock_request):
    response = HTTPResponse(request=mock_request, code=200)
    assert response.time_info == {}
