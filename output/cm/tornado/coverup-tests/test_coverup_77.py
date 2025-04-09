# file tornado/util.py:90-128
# lines [90, 91, 97, 101, 103, 114, 116, 117, 120, 122, 128]
# branches []

import pytest
import zlib
from tornado.util import GzipDecompressor

@pytest.fixture
def gzip_data():
    compressor = zlib.compressobj(wbits=16 + zlib.MAX_WBITS)
    data = b"test data for gzip decompression"
    compressed_data = compressor.compress(data)
    compressed_data += compressor.flush()
    return compressed_data

def test_gzip_decompressor(gzip_data):
    decompressor = GzipDecompressor()

    # Decompress with max_length, should leave an unconsumed tail
    result = decompressor.decompress(gzip_data, max_length=10)
    # We can't assert the exact content due to the nature of compression
    # Just ensure we got some data and there's an unconsumed tail
    assert len(result) > 0
    assert decompressor.unconsumed_tail != b""

    # Decompress the unconsumed tail
    result += decompressor.decompress(decompressor.unconsumed_tail)

    # Flush the remaining data
    remaining_data = decompressor.flush()
    result += remaining_data

    assert result == b"test data for gzip decompression"
