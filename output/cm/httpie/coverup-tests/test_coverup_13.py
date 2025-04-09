# file httpie/output/writer.py:72-90
# lines [72, 82, 83, 84, 85, 86, 88, 89, 90]
# branches ['84->exit', '84->85', '85->86', '85->88', '89->84', '89->90']

import io
import pytest
from unittest.mock import Mock

# Assuming the existence of the `write_stream_with_colors_win_py3` function in writer.py
from httpie.output.writer import write_stream_with_colors_win_py3

@pytest.fixture
def mock_stream():
    return [b'\x1b[31mred\x1b[0m', b'plain text', b'\x1b[32mgreen\x1b[0m']

@pytest.fixture
def mock_outfile(mocker):
    outfile = mocker.Mock()
    outfile.buffer = io.BytesIO()
    outfile.encoding = 'utf-8'
    outfile.write = Mock()
    outfile.flush = Mock()
    return outfile

def test_write_stream_with_colors_win_py3(mock_stream, mock_outfile):
    write_stream_with_colors_win_py3(mock_stream, mock_outfile, flush=True)
    
    # Check if the colorized chunks are written as text
    mock_outfile.write.assert_any_call('\x1b[31mred\x1b[0m')
    mock_outfile.write.assert_any_call('\x1b[32mgreen\x1b[0m')
    
    # Check if the non-colorized chunk is written to the buffer
    assert b'plain text' in mock_outfile.buffer.getvalue()
    
    # Check if flush was called
    mock_outfile.flush.assert_called()
