# file: tornado/simple_httpclient.py:293-447
# asked: {"lines": [293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 306, 308, 309, 311, 312, 314, 316, 318, 319, 320, 321, 323, 324, 325, 328, 329, 330, 331, 333, 334, 335, 336, 338, 339, 340, 341, 342, 343, 344, 347, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 361, 362, 363, 365, 366, 373, 374, 375, 376, 377, 378, 379, 380, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 399, 400, 401, 402, 403, 407, 408, 409, 410, 412, 413, 415, 416, 418, 420, 421, 422, 425, 426, 427, 428, 430, 431, 432, 433, 434, 435, 436, 438, 439, 440, 441, 442, 444, 445, 446, 447], "branches": [[296, 297], [296, 300], [301, 302], [301, 303], [304, 305], [304, 306], [306, 308], [306, 309], [311, 312], [311, 314], [319, 320], [319, 328], [320, 321], [320, 323], [333, 334], [333, 338], [347, 349], [347, 351], [354, 355], [354, 356], [356, 357], [356, 361], [361, 365], [361, 366], [366, 373], [366, 375], [373, 366], [373, 374], [375, 376], [375, 377], [377, 378], [377, 384], [378, 379], [378, 383], [385, 386], [385, 387], [387, 388], [387, 390], [390, 391], [390, 399], [392, 393], [392, 394], [399, 400], [399, 401], [401, 402], [401, 403], [403, 407], [403, 420], [412, 415], [412, 420], [420, 421], [420, 422], [422, 425], [422, 426], [426, 430], [426, 433], [433, 434], [433, 435], [441, 442], [441, 444], [446, 0], [446, 447]]}
# gained: {"lines": [293], "branches": []}

import pytest
from tornado.httpclient import HTTPRequest
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from unittest.mock import MagicMock, patch
import socket
import urllib.parse

@pytest.mark.gen_test
async def test_http_connection_run():
    request = HTTPRequest(
        url="http://example.com",
        method="GET",
        headers={},
        connect_timeout=10,
        request_timeout=20,
        allow_ipv6=True,
        decompress_response=True,
    )
    release_callback = MagicMock()
    final_callback = MagicMock()
    tcp_client = TCPClient()
    max_buffer_size = 104857600
    max_header_size = 104857600
    max_body_size = 104857600

    connection = _HTTPConnection(
        client=None,
        request=request,
        release_callback=release_callback,
        final_callback=final_callback,
        max_buffer_size=max_buffer_size,
        tcp_client=tcp_client,
        max_header_size=max_header_size,
        max_body_size=max_body_size,
    )

    with patch.object(tcp_client, 'connect', return_value=MagicMock()) as mock_connect, \
         patch.object(connection, '_get_ssl_options', return_value=None), \
         patch.object(connection, '_create_connection', return_value=MagicMock()), \
         patch.object(connection, '_write_body', return_value=None), \
         patch.object(connection, '_handle_exception', return_value=False), \
         patch.object(connection.io_loop, 'add_timeout', return_value=None), \
         patch.object(connection, '_remove_timeout', return_value=None):

        await connection.run()

        assert connection.parsed.scheme == "http"
        assert connection.parsed.netloc == "example.com"
        assert connection.parsed_hostname == "example.com"
        assert connection.request.headers["Connection"] == "close"
        assert connection.request.headers["Host"] == "example.com"
        assert connection.request.headers["User-Agent"].startswith("Tornado/")
        assert connection.request.headers["Accept-Encoding"] == "gzip"
        assert mock_connect.called
        assert connection._timeout is not None
        assert connection.stream.set_close_callback.called
        assert connection._remove_timeout.called
