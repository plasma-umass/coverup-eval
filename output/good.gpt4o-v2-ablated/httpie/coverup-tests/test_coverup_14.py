# file: httpie/output/streams.py:75-86
# asked: {"lines": [75, 76, 78, 79, 81, 82, 83, 85, 86], "branches": []}
# gained: {"lines": [75, 76, 78, 79, 81, 82, 83, 85, 86], "branches": []}

import pytest
from httpie.output.streams import RawStream
from unittest.mock import MagicMock

@pytest.fixture
def mock_message():
    mock_msg = MagicMock()
    mock_msg.iter_body = MagicMock(return_value=[b'chunk1', b'chunk2'])
    return mock_msg

def test_raw_stream_default_chunk_size(mock_message):
    stream = RawStream(msg=mock_message)
    chunks = list(stream.iter_body())
    assert chunks == [b'chunk1', b'chunk2']
    mock_message.iter_body.assert_called_once_with(RawStream.CHUNK_SIZE)

def test_raw_stream_custom_chunk_size(mock_message):
    custom_chunk_size = 512
    stream = RawStream(chunk_size=custom_chunk_size, msg=mock_message)
    chunks = list(stream.iter_body())
    assert chunks == [b'chunk1', b'chunk2']
    mock_message.iter_body.assert_called_once_with(custom_chunk_size)
