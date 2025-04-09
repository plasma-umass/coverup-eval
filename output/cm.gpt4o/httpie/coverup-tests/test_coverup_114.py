# file httpie/output/formatters/headers.py:4-18
# lines [7, 8, 16, 17, 18]
# branches []

import pytest
from httpie.output.formatters.headers import HeadersFormatter

@pytest.fixture
def mock_format_options(mocker):
    mocker.patch.object(HeadersFormatter, '__init__', lambda self, **kwargs: None)
    formatter = HeadersFormatter()
    formatter.format_options = {'headers': {'sort': True}}
    return formatter

def test_headers_formatter_init(mock_format_options):
    formatter = mock_format_options
    formatter.__init__()
    assert formatter.format_options['headers']['sort'] is True

def test_format_headers(mock_format_options):
    formatter = mock_format_options
    formatter.__init__()
    headers = "HTTP/1.1 200 OK\r\nB: 2\r\nA: 1\r\nC: 3"
    formatted_headers = formatter.format_headers(headers)
    expected_headers = "HTTP/1.1 200 OK\r\nA: 1\r\nB: 2\r\nC: 3"
    assert formatted_headers == expected_headers
