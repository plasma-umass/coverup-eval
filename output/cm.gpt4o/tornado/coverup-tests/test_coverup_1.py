# file tornado/httpclient.py:629-669
# lines [629, 633, 634, 635, 636, 637, 638, 639, 640, 642, 643, 645, 646, 647, 648, 649, 651, 652, 653, 654, 655, 657, 658, 659, 660, 661, 662, 664, 666, 667, 668, 669]
# branches ['642->643', '642->645', '648->649', '648->651', '654->655', '654->657', '659->660', '659->666', '660->661', '660->664']

import pytest
from tornado.httpclient import HTTPRequest, HTTPResponse, HTTPError
from tornado.httputil import HTTPHeaders
from io import BytesIO

def test_http_response():
    request = HTTPRequest(url="http://example.com")
    code = 404
    headers = HTTPHeaders({"Content-Type": "text/html"})
    buffer = BytesIO(b"Not Found")
    effective_url = "http://example.com/notfound"
    error = None
    request_time = 0.5
    time_info = {"starttransfer": 0.2}
    reason = "Not Found"
    start_time = 0.1

    response = HTTPResponse(
        request=request,
        code=code,
        headers=headers,
        buffer=buffer,
        effective_url=effective_url,
        error=error,
        request_time=request_time,
        time_info=time_info,
        reason=reason,
        start_time=start_time,
    )

    assert response.request == request
    assert response.code == code
    assert response.reason == reason
    assert response.headers == headers
    assert response.buffer == buffer
    assert response.effective_url == effective_url
    assert response.error is not None
    assert isinstance(response.error, HTTPError)
    assert response.error.code == code
    assert response.request_time == request_time
    assert response.time_info == time_info
    assert response.start_time == start_time

    # Test with default values
    response_default = HTTPResponse(request=request, code=200)
    assert response_default.request == request
    assert response_default.code == 200
    assert response_default.reason == "OK"
    assert isinstance(response_default.headers, HTTPHeaders)
    assert response_default.buffer is None
    assert response_default.effective_url == request.url
    assert response_default.error is None
    assert response_default.request_time is None
    assert response_default.time_info == {}
    assert response_default.start_time is None
