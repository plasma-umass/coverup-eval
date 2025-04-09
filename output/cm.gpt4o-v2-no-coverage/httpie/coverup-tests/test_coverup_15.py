# file: httpie/output/writer.py:54-69
# asked: {"lines": [54, 60, 62, 63, 64, 66, 67, 68, 69], "branches": [[66, 0], [66, 67], [68, 66], [68, 69]]}
# gained: {"lines": [54, 60, 62, 63, 64, 66, 67, 68, 69], "branches": [[66, 0], [66, 67], [68, 66], [68, 69]]}

import pytest
from unittest.mock import Mock, MagicMock
from httpie.output.writer import write_stream
from httpie.output.streams import BaseStream
from typing import TextIO

class MockStream(BaseStream):
    def __iter__(self):
        return iter([b'chunk1', b'chunk2'])

def test_write_stream_with_buffer():
    mock_outfile = MagicMock()
    mock_outfile.buffer = mock_outfile
    stream = MockStream(None)
    
    write_stream(stream, mock_outfile, flush=True)
    
    assert mock_outfile.write.call_count == 2
    mock_outfile.write.assert_any_call(b'chunk1')
    mock_outfile.write.assert_any_call(b'chunk2')
    assert mock_outfile.flush.call_count == 2

def test_write_stream_without_buffer():
    mock_outfile = MagicMock(spec=TextIO)
    del mock_outfile.buffer
    stream = MockStream(None)
    
    write_stream(stream, mock_outfile, flush=False)
    
    assert mock_outfile.write.call_count == 2
    mock_outfile.write.assert_any_call(b'chunk1')
    mock_outfile.write.assert_any_call(b'chunk2')
    mock_outfile.flush.assert_not_called()

def test_write_stream_flush_false():
    mock_outfile = MagicMock()
    mock_outfile.buffer = mock_outfile
    stream = MockStream(None)
    
    write_stream(stream, mock_outfile, flush=False)
    
    assert mock_outfile.write.call_count == 2
    mock_outfile.write.assert_any_call(b'chunk1')
    mock_outfile.write.assert_any_call(b'chunk2')
    mock_outfile.flush.assert_not_called()
