# file: httpie/output/streams.py:75-86
# asked: {"lines": [75, 76, 78, 79, 81, 82, 83, 85, 86], "branches": []}
# gained: {"lines": [75, 76, 78, 79, 81, 82, 83, 85, 86], "branches": []}

import pytest
from unittest.mock import MagicMock
from httpie.output.streams import RawStream

@pytest.fixture
def mock_msg():
    return MagicMock()

@pytest.fixture
def raw_stream(mock_msg):
    return RawStream(msg=mock_msg)

def test_raw_stream_default_chunk_size(raw_stream, mock_msg):
    mock_msg.iter_body.return_value = [b'chunk1', b'chunk2']
    chunks = list(raw_stream.iter_body())
    assert chunks == [b'chunk1', b'chunk2']
    mock_msg.iter_body.assert_called_once_with(RawStream.CHUNK_SIZE)

def test_raw_stream_custom_chunk_size(mock_msg):
    custom_chunk_size = 2048
    raw_stream = RawStream(chunk_size=custom_chunk_size, msg=mock_msg)
    mock_msg.iter_body.return_value = [b'chunk1', b'chunk2']
    chunks = list(raw_stream.iter_body())
    assert chunks == [b'chunk1', b'chunk2']
    mock_msg.iter_body.assert_called_once_with(custom_chunk_size)
