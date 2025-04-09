# file: httpie/output/writer.py:72-90
# asked: {"lines": [82, 83, 84, 85, 86, 88, 89, 90], "branches": [[84, 0], [84, 85], [85, 86], [85, 88], [89, 84], [89, 90]]}
# gained: {"lines": [82, 83, 84, 85, 86, 88, 89, 90], "branches": [[84, 0], [84, 85], [85, 86], [85, 88], [89, 84], [89, 90]]}

import pytest
from io import BytesIO, StringIO
from unittest.mock import MagicMock
from httpie.output.writer import write_stream_with_colors_win_py3
from httpie.output.streams import BaseStream

class MockStream(BaseStream):
    def __init__(self, chunks):
        self.chunks = chunks

    def __iter__(self):
        return iter(self.chunks)

@pytest.fixture
def mock_stream():
    return MockStream([b'\x1b[31mRed', b' text', b'\x1b[0m', b' normal'])

@pytest.fixture
def mock_outfile():
    outfile = MagicMock()
    outfile.encoding = 'utf-8'
    outfile.buffer = BytesIO()
    return outfile

def test_write_stream_with_colors_win_py3_with_color(mock_stream, mock_outfile):
    write_stream_with_colors_win_py3(mock_stream, mock_outfile, flush=True)
    
    # Check that the colorized chunks are written as text
    mock_outfile.write.assert_any_call('\x1b[31mRed')
    mock_outfile.write.assert_any_call('\x1b[0m')
    
    # Check that the non-colorized chunks are written to the buffer
    assert mock_outfile.buffer.getvalue() == b' text normal'

    # Check that flush was called
    assert mock_outfile.flush.call_count == 4

def test_write_stream_with_colors_win_py3_without_color(mock_outfile):
    stream = MockStream([b'normal text'])
    write_stream_with_colors_win_py3(stream, mock_outfile, flush=False)
    
    # Check that the non-colorized chunks are written to the buffer
    assert mock_outfile.buffer.getvalue() == b'normal text'
    
    # Check that flush was not called
    mock_outfile.flush.assert_not_called()
