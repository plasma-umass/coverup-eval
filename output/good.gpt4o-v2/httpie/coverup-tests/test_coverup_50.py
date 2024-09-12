# file: httpie/output/formatters/headers.py:4-18
# asked: {"lines": [4, 6, 7, 8, 10, 16, 17, 18], "branches": []}
# gained: {"lines": [4, 6, 7, 8, 10, 16, 17, 18], "branches": []}

import pytest
from httpie.output.formatters.headers import HeadersFormatter

@pytest.fixture
def formatter():
    format_options = {'headers': {'sort': True}}
    return HeadersFormatter(format_options=format_options)

def test_headers_formatter_init(formatter):
    assert formatter.enabled is True

def test_format_headers(formatter):
    headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: 123\r\n"
    expected = "HTTP/1.1 200 OK\r\nContent-Length: 123\r\nContent-Type: text/html"
    assert formatter.format_headers(headers) == expected
