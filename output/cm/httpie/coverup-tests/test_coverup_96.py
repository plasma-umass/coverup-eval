# file httpie/models.py:5-40
# lines [13, 17, 22, 27, 32]
# branches ['38->40']

import pytest
from httpie.models import HTTPMessage
from collections.abc import Iterable
from typing import Optional

class MockHTTPMessage(HTTPMessage):
    def iter_body(self, chunk_size: int) -> Iterable[bytes]:
        return super().iter_body(chunk_size)

    def iter_lines(self, chunk_size: int) -> Iterable[bytes]:
        return super().iter_lines(chunk_size)

    @property
    def headers(self) -> str:
        return super().headers

    @property
    def encoding(self) -> Optional[str]:
        return super().encoding

    @property
    def body(self) -> bytes:
        return super().body

@pytest.fixture
def mock_http_message(mocker):
    mock_orig = mocker.Mock()
    mock_orig.headers = {'Content-Type': b'application/octet-stream'}
    return MockHTTPMessage(mock_orig)

def test_http_message_iter_body_not_implemented(mock_http_message):
    with pytest.raises(NotImplementedError):
        next(mock_http_message.iter_body(1))

def test_http_message_iter_lines_not_implemented(mock_http_message):
    with pytest.raises(NotImplementedError):
        next(mock_http_message.iter_lines(1))

def test_http_message_headers_not_implemented(mock_http_message):
    with pytest.raises(NotImplementedError):
        _ = mock_http_message.headers

def test_http_message_encoding_not_implemented(mock_http_message):
    with pytest.raises(NotImplementedError):
        _ = mock_http_message.encoding

def test_http_message_body_not_implemented(mock_http_message):
    with pytest.raises(NotImplementedError):
        _ = mock_http_message.body

def test_http_message_content_type(mock_http_message):
    assert mock_http_message.content_type == 'application/octet-stream'
