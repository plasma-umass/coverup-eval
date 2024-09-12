# file: httpie/output/writer.py:54-69
# asked: {"lines": [], "branches": [[68, 66]]}
# gained: {"lines": [], "branches": [[68, 66]]}

import pytest
from unittest.mock import MagicMock, call
from httpie.output.writer import write_stream
from httpie.output.streams import BaseStream

class MockStream(BaseStream):
    def __iter__(self):
        return iter([b'chunk1', b'chunk2'])

def test_write_stream_flush():
    mock_outfile = MagicMock()
    mock_outfile.buffer = mock_outfile
    stream = MockStream(None)
    
    write_stream(stream, mock_outfile, flush=True)
    
    expected_calls = [call.write(b'chunk1'), call.flush(), call.write(b'chunk2'), call.flush()]
    assert mock_outfile.mock_calls == expected_calls

def test_write_stream_no_flush():
    mock_outfile = MagicMock()
    mock_outfile.buffer = mock_outfile
    stream = MockStream(None)
    
    write_stream(stream, mock_outfile, flush=False)
    
    expected_calls = [call.write(b'chunk1'), call.write(b'chunk2')]
    assert mock_outfile.mock_calls == expected_calls
