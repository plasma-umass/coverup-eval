# file tornado/simple_httpclient.py:622-682
# lines [622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 633, 634, 644, 645, 647, 648, 649, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 681, 682]
# branches ['627->628', '627->667', '644->647', '644->659', '649->655', '649->659', '667->668', '667->670']

import pytest
from unittest import mock
from tornado.simple_httpclient import SimpleAsyncHTTPClient, HTTPResponse, _RequestProxy
from tornado.httputil import HTTPHeaders
from tornado.ioloop import IOLoop
from tornado.httpclient import HTTPRequest
from io import BytesIO
import urllib.parse
import copy

@pytest.mark.asyncio
async def test_http_connection_finish_redirect(mocker):
    io_loop = IOLoop.current()
    client = SimpleAsyncHTTPClient(io_loop=io_loop)
    request = HTTPRequest(url="http://example.com", method="POST", max_redirects=1)
    proxy_request = _RequestProxy(request, {})
    connection = client._HTTPConnection(client, request, proxy_request, io_loop, mock.Mock())

    connection.code = 302
    connection.headers = HTTPHeaders({"Location": "http://example.com/redirect"})
    connection.chunks = [b"chunk1", b"chunk2"]
    connection.request = proxy_request
    connection.final_callback = mock.Mock()
    connection._should_follow_redirect = mock.Mock(return_value=True)
    connection._remove_timeout = mock.Mock()
    connection._release = mock.Mock()
    connection._on_end_request = mock.Mock()

    await connection.finish()

    assert connection._remove_timeout.called
    assert connection._release.called
    assert connection._on_end_request.called
    assert connection.final_callback.called

@pytest.mark.asyncio
async def test_http_connection_finish_no_redirect(mocker):
    io_loop = IOLoop.current()
    client = SimpleAsyncHTTPClient(io_loop=io_loop)
    request = HTTPRequest(url="http://example.com", method="GET")
    proxy_request = _RequestProxy(request, {})
    connection = client._HTTPConnection(client, request, proxy_request, io_loop, mock.Mock())

    connection.code = 200
    connection.headers = HTTPHeaders()
    connection.chunks = [b"chunk1", b"chunk2"]
    connection.request = proxy_request
    connection.final_callback = mock.Mock()
    connection._should_follow_redirect = mock.Mock(return_value=False)
    connection._remove_timeout = mock.Mock()
    connection._release = mock.Mock()
    connection._on_end_request = mock.Mock()

    await connection.finish()

    assert connection._remove_timeout.called
    assert connection._on_end_request.called
    assert connection.final_callback.called
    response = connection.final_callback.call_args[0][0]
    assert isinstance(response, HTTPResponse)
    assert response.code == 200
    assert response.body == b"chunk1chunk2"
    assert response.request_time > 0
    assert response.effective_url == "http://example.com"
