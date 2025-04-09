# file: tornado/util.py:90-128
# asked: {"lines": [90, 91, 97, 101, 103, 114, 116, 117, 120, 122, 128], "branches": []}
# gained: {"lines": [90, 91, 97, 101, 103, 114, 116, 117, 120, 122, 128], "branches": []}

import pytest
import zlib
from tornado.util import GzipDecompressor

@pytest.fixture
def gzip_data():
    compressor = zlib.compressobj(wbits=16 + zlib.MAX_WBITS)
    data = compressor.compress(b"Test data") + compressor.flush()
    return data

def test_gzip_decompressor_decompress(gzip_data):
    decompressor = GzipDecompressor()
    result = decompressor.decompress(gzip_data)
    assert result == b"Test data"

def test_gzip_decompressor_unconsumed_tail(gzip_data):
    decompressor = GzipDecompressor()
    decompressor.decompress(gzip_data, max_length=4)
    assert decompressor.unconsumed_tail != b""

def test_gzip_decompressor_flush(gzip_data):
    decompressor = GzipDecompressor()
    decompressor.decompress(gzip_data)
    result = decompressor.flush()
    assert result == b""
