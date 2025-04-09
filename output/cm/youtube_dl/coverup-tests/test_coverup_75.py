# file youtube_dl/downloader/f4m.py:210-211
# lines [211]
# branches []

import pytest
from youtube_dl.downloader.f4m import write_unsigned_int
from youtube_dl.compat import compat_struct_pack
from io import BytesIO

def test_write_unsigned_int():
    # Create a mock stream using BytesIO
    mock_stream = BytesIO()

    # Call the function that needs to be tested
    write_unsigned_int(mock_stream, 123456789)

    # Reset the stream position to the beginning
    mock_stream.seek(0)

    # Read the written bytes
    written_bytes = mock_stream.read()

    # Expected bytes after packing the integer 123456789
    expected_bytes = compat_struct_pack('!I', 123456789)

    # Assert that the written bytes match the expected bytes
    assert written_bytes == expected_bytes

    # Clean up the mock stream
    mock_stream.close()
