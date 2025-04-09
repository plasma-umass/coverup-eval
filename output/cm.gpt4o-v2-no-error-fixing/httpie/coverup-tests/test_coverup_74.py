# file: httpie/models.py:43-86
# asked: {"lines": [47, 50, 55, 57, 58, 59, 60, 61, 62, 64, 65, 66, 69, 70, 71, 74, 76, 80, 86], "branches": []}
# gained: {"lines": [47, 50, 55, 57, 58, 59, 60, 61, 62, 64, 65, 66, 69, 70, 76, 80, 86], "branches": []}

import pytest
from unittest.mock import Mock

class TestHTTPResponse:
    
    @pytest.fixture
    def mock_response(self):
        mock_response = Mock()
        mock_response.iter_content = Mock(return_value=iter([b'chunk1', b'chunk2']))
        mock_response.iter_lines = Mock(return_value=iter([b'line1', b'line2']))
        mock_response.raw._original_response.version = 11
        mock_response.raw._original_response.status = 200
        mock_response.raw._original_response.reason = 'OK'
        mock_response.raw._original_response.msg._headers = [('Content-Type', 'application/json')]
        mock_response.raw._original_response.msg.headers = ['Content-Type: application/json\r\n']
        mock_response.encoding = 'utf8'
        mock_response.content = b'{"key": "value"}'
        return mock_response

    @pytest.fixture
    def http_response(self, mock_response):
        from httpie.models import HTTPResponse
        return HTTPResponse(mock_response)

    def test_iter_body(self, http_response):
        chunks = list(http_response.iter_body(chunk_size=1))
        assert chunks == [b'chunk1', b'chunk2']

    def test_iter_lines(self, http_response):
        lines = list(http_response.iter_lines(chunk_size=1))
        assert lines == [(b'line1', b'\n'), (b'line2', b'\n')]

    def test_headers(self, http_response):
        headers = http_response.headers
        assert headers == 'HTTP/1.1 200 OK\r\nContent-Type: application/json'

    def test_encoding(self, http_response):
        encoding = http_response.encoding
        assert encoding == 'utf8'

    def test_body(self, http_response):
        body = http_response.body
        assert body == b'{"key": "value"}'
