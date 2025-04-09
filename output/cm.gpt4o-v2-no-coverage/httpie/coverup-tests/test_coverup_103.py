# file: httpie/output/formatters/headers.py:4-18
# asked: {"lines": [7, 8, 16, 17, 18], "branches": []}
# gained: {"lines": [7, 8, 16, 17, 18], "branches": []}

import pytest
from httpie.output.formatters.headers import HeadersFormatter

@pytest.fixture
def formatter():
    format_options = {'headers': {'sort': True}}
    return HeadersFormatter(format_options=format_options)

def test_init(formatter):
    assert formatter.enabled is True

def test_format_headers(formatter):
    headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: 1234\r\n"
    expected = "HTTP/1.1 200 OK\r\nContent-Length: 1234\r\nContent-Type: text/html"
    assert formatter.format_headers(headers) == expected

def test_format_headers_with_multiple_same_name(formatter):
    headers = "HTTP/1.1 200 OK\r\nSet-Cookie: id=a3fWa\r\nSet-Cookie: lang=en-US\r\nContent-Type: text/html\r\n"
    expected = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nSet-Cookie: id=a3fWa\r\nSet-Cookie: lang=en-US"
    assert formatter.format_headers(headers) == expected
