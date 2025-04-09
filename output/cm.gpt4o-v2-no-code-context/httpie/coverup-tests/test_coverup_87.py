# file: httpie/output/formatters/headers.py:4-18
# asked: {"lines": [7, 8], "branches": []}
# gained: {"lines": [7, 8], "branches": []}

import pytest
from httpie.output.formatters.headers import HeadersFormatter

class MockFormatterPlugin:
    def __init__(self, **kwargs):
        self.format_options = kwargs.get('format_options', {})

@pytest.fixture
def mock_formatter_plugin(monkeypatch):
    monkeypatch.setattr('httpie.output.formatters.headers.FormatterPlugin', MockFormatterPlugin)

def test_headers_formatter_init_with_sort_enabled(mock_formatter_plugin):
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    assert formatter.enabled is True

def test_headers_formatter_init_with_sort_disabled(mock_formatter_plugin):
    formatter = HeadersFormatter(format_options={'headers': {'sort': False}})
    assert formatter.enabled is False

def test_format_headers(mock_formatter_plugin):
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    headers = "HTTP/1.1 200 OK\r\nB: value\r\nA: value"
    formatted_headers = formatter.format_headers(headers)
    assert formatted_headers == "HTTP/1.1 200 OK\r\nA: value\r\nB: value"
