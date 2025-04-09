# file: httpie/output/formatters/headers.py:4-18
# asked: {"lines": [7, 8, 16, 17, 18], "branches": []}
# gained: {"lines": [16, 17, 18], "branches": []}

import pytest
from httpie.output.formatters.headers import HeadersFormatter

@pytest.fixture
def formatter(monkeypatch):
    # Mock the format_options to ensure the 'headers' key exists with 'sort' option
    monkeypatch.setattr(HeadersFormatter, '__init__', lambda self, **kwargs: None)
    formatter = HeadersFormatter()
    formatter.format_options = {'headers': {'sort': True}}
    formatter.enabled = formatter.format_options['headers']['sort']
    return formatter

def test_init(formatter):
    # Test the __init__ method to ensure it sets self.enabled correctly
    assert formatter.enabled is True

def test_format_headers(formatter):
    # Test the format_headers method to ensure it sorts headers correctly
    input_headers = "HTTP/1.1 200 OK\r\nB-Header: value2\r\nA-Header: value1\r\nC-Header: value3"
    expected_output = "HTTP/1.1 200 OK\r\nA-Header: value1\r\nB-Header: value2\r\nC-Header: value3"
    assert formatter.format_headers(input_headers) == expected_output

def test_format_headers_empty(formatter):
    # Test the format_headers method with empty headers
    input_headers = "HTTP/1.1 200 OK"
    expected_output = "HTTP/1.1 200 OK"
    assert formatter.format_headers(input_headers) == expected_output
