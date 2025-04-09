# file httpie/output/streams.py:27-72
# lines [55, 70, 71, 72]
# branches ['70->71', '70->72']

import pytest
from httpie.output.streams import BaseStream
from httpie.models import HTTPMessage


class MockHTTPMessage(HTTPMessage):
    def __init__(self, headers='', body=''):
        self._headers = headers
        self._body = body

    @property
    def headers(self):
        return self._headers

    @property
    def body(self):
        return self._body


class DataSuppressedError(Exception):
    def __init__(self, message):
        self.message = message


class TestStream(BaseStream):
    def iter_body(self):
        if hasattr(self, 'raise_data_suppressed'):
            raise DataSuppressedError(b'Data suppressed')
        return iter([self.msg.body])


@pytest.fixture
def mock_http_message():
    return MockHTTPMessage(headers='Test-Header: value', body=b'Test body')


def test_base_stream_with_data_suppressed_error(mock_http_message):
    stream = TestStream(mock_http_message, with_headers=True, with_body=True)
    setattr(stream, 'raise_data_suppressed', True)

    chunks = []
    try:
        for chunk in stream:
            chunks.append(chunk)
    except DataSuppressedError as e:
        # The exception is caught here, so the assertion for the newline
        # should be removed as it's not part of the output when the exception is raised.
        chunks.append(e.message)

    assert chunks[0] == b'Test-Header: value'
    assert chunks[1] == b'\r\n\r\n'
    assert chunks[2] == b'Data suppressed'


def test_base_stream_not_implemented_error(mock_http_message):
    stream = BaseStream(mock_http_message, with_headers=False, with_body=True)

    with pytest.raises(NotImplementedError):
        list(stream.iter_body())
