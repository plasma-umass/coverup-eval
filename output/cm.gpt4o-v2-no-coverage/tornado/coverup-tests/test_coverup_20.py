# file: tornado/httpclient.py:629-669
# asked: {"lines": [629, 633, 634, 635, 636, 637, 638, 639, 640, 642, 643, 645, 646, 647, 648, 649, 651, 652, 653, 654, 655, 657, 658, 659, 660, 661, 662, 664, 666, 667, 668, 669], "branches": [[642, 643], [642, 645], [648, 649], [648, 651], [654, 655], [654, 657], [659, 660], [659, 666], [660, 661], [660, 664]]}
# gained: {"lines": [629, 633, 634, 635, 636, 637, 638, 639, 640, 642, 643, 645, 646, 647, 648, 649, 651, 652, 653, 654, 655, 657, 658, 659, 660, 661, 662, 664, 666, 667, 668, 669], "branches": [[642, 643], [642, 645], [648, 649], [648, 651], [654, 655], [654, 657], [659, 660], [659, 666], [660, 661], [660, 664]]}

import pytest
from io import BytesIO
from tornado.httpclient import HTTPRequest, HTTPResponse, HTTPError
from tornado.httputil import HTTPHeaders
from tornado.httpclient import _RequestProxy

@pytest.fixture
def sample_request():
    return HTTPRequest(url="http://example.com")

def test_http_response_initialization_with_request_proxy(sample_request):
    request_proxy = _RequestProxy(sample_request, None)
    response = HTTPResponse(request_proxy, 200)
    assert response.request == sample_request

def test_http_response_initialization_with_direct_request(sample_request):
    response = HTTPResponse(sample_request, 200)
    assert response.request == sample_request

def test_http_response_initialization_with_headers(sample_request):
    headers = HTTPHeaders({"Content-Type": "text/html"})
    response = HTTPResponse(sample_request, 200, headers=headers)
    assert response.headers == headers

def test_http_response_initialization_without_headers(sample_request):
    response = HTTPResponse(sample_request, 200)
    assert isinstance(response.headers, HTTPHeaders)

def test_http_response_initialization_with_effective_url(sample_request):
    effective_url = "http://redirected.com"
    response = HTTPResponse(sample_request, 200, effective_url=effective_url)
    assert response.effective_url == effective_url

def test_http_response_initialization_without_effective_url(sample_request):
    response = HTTPResponse(sample_request, 200)
    assert response.effective_url == sample_request.url

def test_http_response_initialization_with_error(sample_request):
    error = HTTPError(500, message="Server Error")
    response = HTTPResponse(sample_request, 500, error=error)
    assert response.error == error

def test_http_response_initialization_without_error(sample_request):
    response = HTTPResponse(sample_request, 500)
    assert isinstance(response.error, HTTPError)
    assert response.error.code == 500

def test_http_response_initialization_with_success_code(sample_request):
    response = HTTPResponse(sample_request, 200)
    assert response.error is None

def test_http_response_initialization_with_reason(sample_request):
    reason = "Custom Reason"
    response = HTTPResponse(sample_request, 200, reason=reason)
    assert response.reason == reason

def test_http_response_initialization_without_reason(sample_request, mocker):
    mocker.patch("tornado.httputil.responses", {200: "OK"})
    response = HTTPResponse(sample_request, 200)
    assert response.reason == "OK"

def test_http_response_initialization_with_time_info(sample_request):
    time_info = {"starttransfer": 0.1}
    response = HTTPResponse(sample_request, 200, time_info=time_info)
    assert response.time_info == time_info

def test_http_response_initialization_without_time_info(sample_request):
    response = HTTPResponse(sample_request, 200)
    assert response.time_info == {}

def test_http_response_initialization_with_start_time(sample_request):
    start_time = 1234567890.0
    response = HTTPResponse(sample_request, 200, start_time=start_time)
    assert response.start_time == start_time

def test_http_response_initialization_with_request_time(sample_request):
    request_time = 1.23
    response = HTTPResponse(sample_request, 200, request_time=request_time)
    assert response.request_time == request_time

def test_http_response_initialization_with_buffer(sample_request):
    buffer = BytesIO(b"test")
    response = HTTPResponse(sample_request, 200, buffer=buffer)
    assert response.buffer == buffer
