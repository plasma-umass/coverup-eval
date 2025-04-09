# file: httpie/output/writer.py:54-69
# asked: {"lines": [60, 62, 63, 64, 66, 67, 68, 69], "branches": [[66, 0], [66, 67], [68, 66], [68, 69]]}
# gained: {"lines": [60, 62, 63, 64, 66, 67, 68, 69], "branches": [[66, 0], [66, 67], [68, 66], [68, 69]]}

import pytest
from io import BytesIO, StringIO
from unittest.mock import MagicMock

class MockStream:
    def __iter__(self):
        return iter([b'chunk1', b'chunk2'])

def test_write_stream_with_buffer():
    stream = MockStream()
    outfile = BytesIO()
    flush = False

    from httpie.output.writer import write_stream
    write_stream(stream, outfile, flush)

    assert outfile.getvalue() == b'chunk1chunk2'

def test_write_stream_without_buffer():
    stream = MockStream()
    outfile = BytesIO()  # Use BytesIO instead of StringIO to handle bytes
    flush = False

    from httpie.output.writer import write_stream
    write_stream(stream, outfile, flush)

    assert outfile.getvalue() == b'chunk1chunk2'

def test_write_stream_with_flush():
    stream = MockStream()
    outfile = MagicMock()
    outfile.buffer = BytesIO()
    flush = True

    from httpie.output.writer import write_stream
    write_stream(stream, outfile, flush)

    assert outfile.buffer.getvalue() == b'chunk1chunk2'
    assert outfile.flush.call_count == 2
