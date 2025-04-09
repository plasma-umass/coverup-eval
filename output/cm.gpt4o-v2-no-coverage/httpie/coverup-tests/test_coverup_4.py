# file: httpie/models.py:89-138
# asked: {"lines": [89, 90, 92, 93, 95, 96, 98, 99, 100, 102, 103, 104, 105, 108, 109, 110, 112, 113, 114, 115, 117, 120, 121, 123, 125, 126, 128, 129, 130, 132, 133, 134, 135, 137, 138], "branches": [[109, 110], [109, 112], [123, 125], [123, 126], [135, 137], [135, 138]]}
# gained: {"lines": [89, 90, 92, 93, 95, 96, 98, 99, 100, 102, 103, 104, 105, 108, 109, 110, 112, 113, 114, 115, 117, 120, 121, 123, 126, 128, 129, 130, 132, 133, 134, 135, 137, 138], "branches": [[109, 110], [123, 126], [135, 137], [135, 138]]}

import pytest
from unittest.mock import Mock
from httpie.models import HTTPRequest
from urllib.parse import urlsplit

class TestHTTPRequest:
    
    @pytest.fixture
    def mock_request(self):
        mock_request = Mock()
        mock_request.method = 'GET'
        mock_request.url = 'http://example.com/path?query=1'
        mock_request.headers = {'User-Agent': 'test-agent'}
        mock_request.body = 'test body'
        return mock_request

    def test_iter_body(self, mock_request):
        request = HTTPRequest(mock_request)
        body = next(request.iter_body(1024))
        assert body == b'test body'

    def test_iter_lines(self, mock_request):
        request = HTTPRequest(mock_request)
        lines = next(request.iter_lines(1024))
        assert lines == (b'test body', b'')

    def test_headers(self, mock_request):
        request = HTTPRequest(mock_request)
        headers = request.headers
        assert 'GET /path?query=1 HTTP/1.1' in headers
        assert 'User-Agent: test-agent' in headers
        assert 'Host: example.com' in headers

    def test_encoding(self, mock_request):
        request = HTTPRequest(mock_request)
        assert request.encoding == 'utf8'

    def test_body(self, mock_request):
        request = HTTPRequest(mock_request)
        assert request.body == b'test body'

    def test_body_empty(self, mock_request):
        mock_request.body = None
        request = HTTPRequest(mock_request)
        assert request.body == b''

    def test_headers_no_host(self, mock_request):
        mock_request.headers = {}
        request = HTTPRequest(mock_request)
        headers = request.headers
        assert 'Host: example.com' in headers
