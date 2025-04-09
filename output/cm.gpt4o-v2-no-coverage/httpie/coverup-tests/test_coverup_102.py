# file: httpie/output/streams.py:27-72
# asked: {"lines": [51, 55, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], "branches": [[59, 60], [59, 63], [63, 0], [63, 64], [65, 0], [65, 66], [67, 65], [67, 68], [70, 71], [70, 72]]}
# gained: {"lines": [51, 55, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], "branches": [[59, 60], [59, 63], [63, 0], [63, 64], [65, 0], [65, 66], [67, 65], [67, 68], [70, 71]]}

import pytest
from unittest.mock import Mock, call
from httpie.output.streams import BaseStream, DataSuppressedError
from httpie.models import HTTPMessage

class MockHTTPMessage(HTTPMessage):
    def __init__(self, headers, body):
        self._headers = headers
        self._body = body

    @property
    def headers(self):
        return self._headers

    @property
    def body(self):
        return self._body

class TestBaseStream:
    @pytest.fixture
    def mock_msg(self):
        return MockHTTPMessage(headers="Test-Headers", body=b"Test-Body")

    def test_init(self, mock_msg):
        stream = BaseStream(mock_msg, with_headers=True, with_body=True)
        assert stream.msg == mock_msg
        assert stream.with_headers is True
        assert stream.with_body is True
        assert stream.on_body_chunk_downloaded is None

    def test_get_headers(self, mock_msg):
        stream = BaseStream(mock_msg, with_headers=True, with_body=True)
        assert stream.get_headers() == b"Test-Headers"

    def test_iter_body_not_implemented(self, mock_msg):
        stream = BaseStream(mock_msg, with_headers=True, with_body=True)
        with pytest.raises(NotImplementedError):
            list(stream.iter_body())

    def test_iter_with_headers_and_body(self, mock_msg, monkeypatch):
        stream = BaseStream(mock_msg, with_headers=True, with_body=True)
        mock_iter_body = Mock(return_value=[b"chunk1", b"chunk2"])
        monkeypatch.setattr(stream, "iter_body", mock_iter_body)
        result = list(stream)
        assert result == [b"Test-Headers", b"\r\n\r\n", b"chunk1", b"chunk2"]

    def test_iter_with_headers_only(self, mock_msg, monkeypatch):
        stream = BaseStream(mock_msg, with_headers=True, with_body=False)
        result = list(stream)
        assert result == [b"Test-Headers", b"\r\n\r\n"]

    def test_iter_with_body_only(self, mock_msg, monkeypatch):
        stream = BaseStream(mock_msg, with_headers=False, with_body=True)
        mock_iter_body = Mock(return_value=[b"chunk1", b"chunk2"])
        monkeypatch.setattr(stream, "iter_body", mock_iter_body)
        result = list(stream)
        assert result == [b"chunk1", b"chunk2"]

    def test_iter_with_data_suppressed_error(self, mock_msg, monkeypatch):
        stream = BaseStream(mock_msg, with_headers=True, with_body=True)
        mock_iter_body = Mock(side_effect=DataSuppressedError())
        monkeypatch.setattr(stream, "iter_body", mock_iter_body)
        result = list(stream)
        assert result == [b"Test-Headers", b"\r\n\r\n", b"\n", None]

    def test_on_body_chunk_downloaded(self, mock_msg, monkeypatch):
        mock_callback = Mock()
        stream = BaseStream(mock_msg, with_headers=True, with_body=True, on_body_chunk_downloaded=mock_callback)
        mock_iter_body = Mock(return_value=[b"chunk1", b"chunk2"])
        monkeypatch.setattr(stream, "iter_body", mock_iter_body)
        result = list(stream)
        assert result == [b"Test-Headers", b"\r\n\r\n", b"chunk1", b"chunk2"]
        mock_callback.assert_has_calls([call(b"chunk1"), call(b"chunk2")])
