# file httpie/output/streams.py:75-86
# lines [75, 76, 78, 79, 81, 82, 83, 85, 86]
# branches []

import pytest
from httpie.output.streams import RawStream
from httpie.models import HTTPMessage


@pytest.fixture
def mock_http_message(mocker):
    mock_msg = mocker.Mock(spec=HTTPMessage)
    mock_msg.iter_body.return_value = iter([b'chunk1', b'chunk2', b'chunk3'])
    return mock_msg


def test_raw_stream_iter_body_with_default_chunk_size(mock_http_message):
    stream = RawStream(msg=mock_http_message)
    chunks = list(stream.iter_body())
    assert chunks == [b'chunk1', b'chunk2', b'chunk3']
    mock_http_message.iter_body.assert_called_once_with(RawStream.CHUNK_SIZE)


def test_raw_stream_iter_body_with_custom_chunk_size(mock_http_message):
    custom_chunk_size = 512
    stream = RawStream(msg=mock_http_message, chunk_size=custom_chunk_size)
    chunks = list(stream.iter_body())
    assert chunks == [b'chunk1', b'chunk2', b'chunk3']
    mock_http_message.iter_body.assert_called_once_with(custom_chunk_size)
