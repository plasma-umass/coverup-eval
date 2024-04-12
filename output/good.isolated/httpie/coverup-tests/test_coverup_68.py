# file httpie/output/streams.py:27-72
# lines [27, 28, 30, 33, 34, 35, 43, 44, 45, 46, 47, 49, 51, 53, 55, 57, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]
# branches ['59->60', '59->63', '63->exit', '63->64', '65->exit', '65->66', '67->65', '67->68', '70->71', '70->72']

import pytest
from httpie.output.streams import BaseStream
from httpie.models import HTTPMessage


class DataSuppressedError(Exception):
    def __init__(self, message):
        self.message = message.encode('utf8')


class MockHTTPMessage(HTTPMessage):
    def __init__(self, headers='', body=''):
        self._headers = headers
        self._body = body

    @property
    def headers(self):
        return self._headers

    def iter_body(self):
        yield self._body.encode('utf8')


class MockStream(BaseStream):
    def iter_body(self):
        if self.msg._body == 'raise_data_suppressed':
            raise DataSuppressedError('Data suppressed')
        else:
            yield self.msg._body.encode('utf8')


@pytest.fixture
def mock_http_message():
    return MockHTTPMessage(headers='Test-Header: value', body='Test body')


@pytest.fixture
def mock_stream(mock_http_message):
    return MockStream(msg=mock_http_message)


def test_base_stream_with_headers_and_body(mock_stream):
    chunks = list(mock_stream)
    assert chunks[0] == b'Test-Header: value'
    assert chunks[1] == b'\r\n\r\n'
    assert chunks[2] == b'Test body'


def test_base_stream_with_headers_only(mock_stream):
    mock_stream.with_body = False
    chunks = list(mock_stream)
    assert chunks[0] == b'Test-Header: value'
    assert chunks[1] == b'\r\n\r\n'
    assert len(chunks) == 2


def test_base_stream_with_body_only(mock_stream):
    mock_stream.with_headers = False
    chunks = list(mock_stream)
    assert chunks[0] == b'Test body'


def test_base_stream_with_data_suppressed_error(mock_http_message):
    mock_http_message._body = 'raise_data_suppressed'
    mock_stream = MockStream(msg=mock_http_message, with_headers=True)
    with pytest.raises(DataSuppressedError) as exc_info:
        list(mock_stream)
    assert exc_info.value.message == b'Data suppressed'


def test_base_stream_on_body_chunk_downloaded_callback(mock_stream, mocker):
    callback = mocker.Mock()
    mock_stream.on_body_chunk_downloaded = callback
    list(mock_stream)
    callback.assert_called_once_with(b'Test body')
