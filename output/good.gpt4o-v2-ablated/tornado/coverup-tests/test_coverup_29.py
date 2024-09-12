# file: tornado/util.py:90-128
# asked: {"lines": [90, 91, 97, 101, 103, 114, 116, 117, 120, 122, 128], "branches": []}
# gained: {"lines": [90, 91, 97, 101, 103, 114, 116, 117, 120, 122, 128], "branches": []}

import pytest
import zlib
from tornado.util import GzipDecompressor

@pytest.fixture
def gzip_compressed_data():
    compressor = zlib.compressobj(9, zlib.DEFLATED, zlib.MAX_WBITS | 16)
    data = b"Test data for gzip compression"
    compressed_data = compressor.compress(data) + compressor.flush()
    return compressed_data, data

def test_gzip_decompressor_decompress(gzip_compressed_data):
    compressed_data, original_data = gzip_compressed_data
    decompressor = GzipDecompressor()
    decompressed_data = decompressor.decompress(compressed_data)
    assert decompressed_data == original_data

def test_gzip_decompressor_unconsumed_tail(gzip_compressed_data):
    compressed_data, original_data = gzip_compressed_data
    decompressor = GzipDecompressor()
    decompressor.decompress(compressed_data[:10])
    assert decompressor.unconsumed_tail == b""

def test_gzip_decompressor_flush(gzip_compressed_data):
    compressed_data, original_data = gzip_compressed_data
    decompressor = GzipDecompressor()
    decompressed_data = decompressor.decompress(compressed_data)
    remaining_data = decompressor.flush()
    assert decompressed_data + remaining_data == original_data
