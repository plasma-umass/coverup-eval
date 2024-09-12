# file: httpie/output/writer.py:54-69
# asked: {"lines": [60, 62, 63, 64, 66, 67, 68, 69], "branches": [[66, 0], [66, 67], [68, 66], [68, 69]]}
# gained: {"lines": [60, 62, 63, 64, 66, 67, 68, 69], "branches": [[66, 0], [66, 67], [68, 69]]}

import pytest
from unittest.mock import Mock, MagicMock
from httpie.output.writer import write_stream
from httpie.output.streams import BaseStream

class MockStream(BaseStream):
    def __init__(self, chunks):
        self.chunks = chunks

    def __iter__(self):
        return iter(self.chunks)

def test_write_stream_with_buffer():
    mock_stream = MockStream([b'chunk1', b'chunk2'])
    mock_outfile = MagicMock()
    mock_outfile.buffer = MagicMock()
    
    write_stream(mock_stream, mock_outfile, flush=True)
    
    assert mock_outfile.buffer.write.call_count == 2
    mock_outfile.buffer.write.assert_any_call(b'chunk1')
    mock_outfile.buffer.write.assert_any_call(b'chunk2')
    assert mock_outfile.flush.call_count == 2

def test_write_stream_without_buffer():
    mock_stream = MockStream([b'chunk1', b'chunk2'])
    mock_outfile = MagicMock()
    del mock_outfile.buffer  # Ensure AttributeError is raised
    
    write_stream(mock_stream, mock_outfile, flush=True)
    
    assert mock_outfile.write.call_count == 2
    mock_outfile.write.assert_any_call(b'chunk1')
    mock_outfile.write.assert_any_call(b'chunk2')
    assert mock_outfile.flush.call_count == 2
