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
    headers = "HTTP/1.1 200 OK\r\nb-header: value2\r\na-header: value1"
    expected = "HTTP/1.1 200 OK\r\na-header: value1\r\nb-header: value2"
    assert formatter.format_headers(headers) == expected
