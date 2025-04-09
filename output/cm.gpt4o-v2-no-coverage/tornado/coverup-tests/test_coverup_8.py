# file: tornado/simple_httpclient.py:293-447
# asked: {"lines": [293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 306, 308, 309, 311, 312, 314, 316, 318, 319, 320, 321, 323, 324, 325, 328, 329, 330, 331, 333, 334, 335, 336, 338, 339, 340, 341, 342, 343, 344, 347, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 361, 362, 363, 365, 366, 373, 374, 375, 376, 377, 378, 379, 380, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 399, 400, 401, 402, 403, 407, 408, 409, 410, 412, 413, 415, 416, 418, 420, 421, 422, 425, 426, 427, 428, 430, 431, 432, 433, 434, 435, 436, 438, 439, 440, 441, 442, 444, 445, 446, 447], "branches": [[296, 297], [296, 300], [301, 302], [301, 303], [304, 305], [304, 306], [306, 308], [306, 309], [311, 312], [311, 314], [319, 320], [319, 328], [320, 321], [320, 323], [333, 334], [333, 338], [347, 349], [347, 351], [354, 355], [354, 356], [356, 357], [356, 361], [361, 365], [361, 366], [366, 373], [366, 375], [373, 366], [373, 374], [375, 376], [375, 377], [377, 378], [377, 384], [378, 379], [378, 383], [385, 386], [385, 387], [387, 388], [387, 390], [390, 391], [390, 399], [392, 393], [392, 394], [399, 400], [399, 401], [401, 402], [401, 403], [403, 407], [403, 420], [412, 415], [412, 420], [420, 421], [420, 422], [422, 425], [422, 426], [426, 430], [426, 433], [433, 434], [433, 435], [441, 442], [441, 444], [446, 0], [446, 447]]}
# gained: {"lines": [293], "branches": []}

import pytest
from unittest.mock import Mock, patch, create_autospec
from tornado.httpclient import HTTPRequest, HTTPResponse
from tornado.ioloop import IOLoop
from tornado.iostream import IOStream
from tornado.tcpclient import TCPClient
from tornado.httputil import HTTPHeaders, HTTPMessageDelegate
from tornado.simple_httpclient import _HTTPConnection
import socket
import base64
import re
import urllib.parse

@pytest.fixture
def mock_ioloop():
    with patch('tornado.ioloop.IOLoop.current') as mock:
        yield mock.return_value

@pytest.fixture
def mock_tcp_client():
    return create_autospec(TCPClient)

@pytest.fixture
def mock_request():
    return create_autospec(HTTPRequest)

@pytest.fixture
def mock_stream():
    return create_autospec(IOStream)

@pytest.fixture
def mock_http_response():
    return create_autospec(HTTPResponse)

@pytest.fixture
def connection(mock_ioloop, mock_tcp_client, mock_request):
    return _HTTPConnection(
        client=None,
        request=mock_request,
        release_callback=Mock(),
        final_callback=Mock(),
        max_buffer_size=104857600,
        tcp_client=mock_tcp_client,
        max_header_size=104857600,
        max_body_size=104857600
    )

@pytest.mark.asyncio
async def test_run_success(connection, mock_request, mock_stream, mock_ioloop):
    mock_request.url = "http://example.com"
    mock_request.allow_ipv6 = True
    mock_request.network_interface = None
    mock_request.connect_timeout = 10
    mock_request.request_timeout = 20
    mock_request.method = "GET"
    mock_request.headers = HTTPHeaders()
    mock_request.auth_username = None
    mock_request.auth_password = None
    mock_request.user_agent = None
    mock_request.body = None
    mock_request.body_producer = None
    mock_request.expect_100_continue = False
    mock_request.decompress_response = False
    mock_request.allow_nonstandard_methods = False

    connection.tcp_client.connect = Mock(return_value=mock_stream)
    connection._get_ssl_options = Mock(return_value=None)
    connection._create_connection = Mock(return_value=Mock())
    connection._write_body = Mock()

    await connection.run()

    assert connection.parsed.scheme == "http"
    assert connection.parsed_hostname == "example.com"
    assert connection.stream == mock_stream
    assert "Connection" in mock_request.headers
    assert "Host" in mock_request.headers
    assert "User-Agent" in mock_request.headers

@pytest.mark.asyncio
async def test_run_invalid_scheme(connection, mock_request):
    mock_request.url = "ftp://example.com"

    with pytest.raises(ValueError, match="Unsupported url scheme: ftp://example.com"):
        await connection.run()

@pytest.mark.asyncio
async def test_run_invalid_network_interface(connection, mock_request):
    mock_request.url = "http://example.com"
    mock_request.allow_ipv6 = True
    mock_request.network_interface = "invalid_ip"

    with pytest.raises(ValueError, match="Unrecognized IPv4 or IPv6 address for network_interface, got 'invalid_ip'"):
        await connection.run()

@pytest.mark.asyncio
async def test_run_unsupported_method(connection, mock_request):
    mock_request.url = "http://example.com"
    mock_request.method = "TRACE"
    mock_request.allow_nonstandard_methods = False

    with pytest.raises(KeyError, match="unknown method TRACE"):
        await connection.run()

@pytest.mark.asyncio
async def test_run_body_mismatch(connection, mock_request):
    mock_request.url = "http://example.com"
    mock_request.method = "POST"
    mock_request.body = None
    mock_request.body_producer = None
    mock_request.allow_nonstandard_methods = False

    with pytest.raises(ValueError, match="Body must not be None for method POST"):
        await connection.run()

@pytest.mark.asyncio
async def test_run_authentication(connection, mock_request):
    mock_request.url = "http://example.com"
    mock_request.auth_username = "user"
    mock_request.auth_password = "pass"
    mock_request.headers = HTTPHeaders()

    await connection.run()

    auth_header = mock_request.headers["Authorization"]
    expected_auth = "Basic " + base64.b64encode(b"user:pass").decode()
    assert auth_header == expected_auth
