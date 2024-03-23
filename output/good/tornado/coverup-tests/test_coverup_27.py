# file tornado/httpclient.py:629-669
# lines [629, 633, 634, 635, 636, 637, 638, 639, 640, 642, 643, 645, 646, 647, 648, 649, 651, 652, 653, 654, 655, 657, 658, 659, 660, 661, 662, 664, 666, 667, 668, 669]
# branches ['642->643', '642->645', '648->649', '648->651', '654->655', '654->657', '659->660', '659->666', '660->661', '660->664']

import pytest
from tornado.httpclient import HTTPResponse, HTTPRequest, HTTPError
from tornado import httputil
from io import BytesIO

@pytest.fixture
def mock_request():
    return HTTPRequest(url='http://example.com')

@pytest.fixture
def mock_headers():
    return httputil.HTTPHeaders({'Content-Type': 'text/plain'})

def test_httpresponse_with_error(mock_request, mock_headers):
    error = HTTPError(404, "Not Found")
    response = HTTPResponse(
        request=mock_request,
        code=404,
        headers=mock_headers,
        buffer=BytesIO(b"Error page"),
        effective_url='http://example.com/error',
        error=error,
        request_time=1.0,
        time_info={'queue': 0.1},
        reason="Not Found",
        start_time=0.0
    )

    assert response.request == mock_request
    assert response.code == 404
    assert response.headers == mock_headers
    assert response.buffer.getvalue() == b"Error page"
    assert response.effective_url == 'http://example.com/error'
    assert response.error == error
    assert response.request_time == 1.0
    assert response.time_info == {'queue': 0.1}
    assert response.reason == "Not Found"
    assert response.start_time == 0.0

def test_httpresponse_without_error(mock_request, mock_headers):
    response = HTTPResponse(
        request=mock_request,
        code=200,
        headers=mock_headers,
        buffer=BytesIO(b"Success page"),
        effective_url='http://example.com/success',
        request_time=1.0,
        time_info={'queue': 0.1},
        reason="OK",
        start_time=0.0
    )

    assert response.request == mock_request
    assert response.code == 200
    assert response.headers == mock_headers
    assert response.buffer.getvalue() == b"Success page"
    assert response.effective_url == 'http://example.com/success'
    assert response.error is None
    assert response.request_time == 1.0
    assert response.time_info == {'queue': 0.1}
    assert response.reason == "OK"
    assert response.start_time == 0.0
