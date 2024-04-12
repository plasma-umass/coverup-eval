# file httpie/output/writer.py:54-69
# lines [54, 60, 62, 63, 64, 66, 67, 68, 69]
# branches ['66->exit', '66->67', '68->66', '68->69']

import io
import pytest
from unittest.mock import Mock
from httpie.output.writer import write_stream

class MockStream:
    def __iter__(self):
        yield b'chunk1'
        yield b'chunk2'

@pytest.fixture
def mock_stream():
    return MockStream()

def test_write_stream_with_flush(mock_stream):
    outfile = Mock(spec=io.BufferedWriter)
    write_stream(mock_stream, outfile, True)
    outfile.write.assert_any_call(b'chunk1')
    outfile.write.assert_any_call(b'chunk2')
    outfile.flush.assert_called()

def test_write_stream_without_flush(mock_stream):
    outfile = Mock(spec=io.BufferedWriter)
    write_stream(mock_stream, outfile, False)
    outfile.write.assert_any_call(b'chunk1')
    outfile.write.assert_any_call(b'chunk2')
    outfile.flush.assert_not_called()

def test_write_stream_with_textio(mock_stream):
    text_stream = io.BytesIO()
    write_stream(mock_stream, text_stream, True)
    text_stream.seek(0)
    assert text_stream.read() == b'chunk1chunk2'
    # No need to assert flush on BytesIO, as it does not have a flush method

def test_write_stream_with_textio_without_flush(mock_stream):
    text_stream = io.BytesIO()
    write_stream(mock_stream, text_stream, False)
    text_stream.seek(0)
    assert text_stream.read() == b'chunk1chunk2'
    # No need to assert flush on BytesIO, as it does not have a flush method
