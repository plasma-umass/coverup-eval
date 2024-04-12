# file sanic/headers.py:188-196
# lines [188, 192, 193, 194, 195, 196]
# branches ['193->194', '193->195']

import pytest
from sanic.headers import format_http1_response

@pytest.fixture
def headers():
    return [(b'Content-Type', b'text/plain'), (b'Content-Length', b'123')]

def test_format_http1_response(headers):
    status = 200
    response = format_http1_response(status, headers)
    expected_response = (
        b"HTTP/1.1 200 OK\r\n"
        b"Content-Type: text/plain\r\n"
        b"Content-Length: 123\r\n"
        b"\r\n"
    )
    assert response == expected_response, "The formatted HTTP/1.1 response does not match the expected output."

def test_format_http1_response_with_no_headers():
    status = 404
    response = format_http1_response(status, [])
    expected_response = (
        b"HTTP/1.1 404 Not Found\r\n"
        b"\r\n"
    )
    assert response == expected_response, "The formatted HTTP/1.1 response with no headers does not match the expected output."
