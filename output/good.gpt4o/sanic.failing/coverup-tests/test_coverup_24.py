# file sanic/headers.py:188-196
# lines [188, 192, 193, 194, 195, 196]
# branches ['193->194', '193->195']

import pytest
from sanic.headers import format_http1_response

def test_format_http1_response():
    status = 200
    headers = [(b"Content-Type", b"text/html"), (b"Content-Length", b"1234")]

    response = format_http1_response(status, headers)

    expected_response = (
        b"HTTP/1.1 200 OK\r\n"
        b"Content-Type: text/html\r\n"
        b"Content-Length: 1234\r\n"
        b"\r\n"
    )

    assert response == expected_response
