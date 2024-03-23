# file youtube_dl/downloader/f4m.py:214-215
# lines [214, 215]
# branches []

import pytest
from youtube_dl.downloader.f4m import write_unsigned_int_24
from youtube_dl.compat import compat_struct_pack
import io

def test_write_unsigned_int_24():
    # Create a bytes stream to mock file writing
    mock_stream = io.BytesIO()

    # Value to be written as unsigned int 24
    test_val = 0x123456

    # Expected result after writing 24 bits (3 bytes) of the test_val
    expected_bytes = compat_struct_pack('!I', test_val)[1:]

    # Call the function with the mock stream and the test value
    write_unsigned_int_24(mock_stream, test_val)

    # Seek to the beginning of the stream to read the written bytes
    mock_stream.seek(0)
    written_bytes = mock_stream.read()

    # Assert that the written bytes match the expected bytes
    assert written_bytes == expected_bytes

    # Clean up by closing the mock stream
    mock_stream.close()
