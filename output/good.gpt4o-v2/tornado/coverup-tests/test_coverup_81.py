# file: tornado/util.py:90-128
# asked: {"lines": [90, 91, 97, 101, 103, 114, 116, 117, 120, 122, 128], "branches": []}
# gained: {"lines": [90, 91, 97, 101, 103, 114, 116, 117, 120, 122, 128], "branches": []}

import pytest
import zlib
from tornado.util import GzipDecompressor

def gzip_compress(data: bytes) -> bytes:
    compressor = zlib.compressobj(wbits=16 + zlib.MAX_WBITS)
    compressed_data = compressor.compress(data) + compressor.flush()
    return compressed_data

def test_gzip_decompressor_init():
    decompressor = GzipDecompressor()
    assert hasattr(decompressor.decompressobj, 'decompress')

def test_gzip_decompressor_decompress():
    decompressor = GzipDecompressor()
    data = b"Hello, world!"
    compressed_data = gzip_compress(data)
    decompressed_data = decompressor.decompress(compressed_data)
    assert decompressed_data == data

def test_gzip_decompressor_unconsumed_tail():
    decompressor = GzipDecompressor()
    data = b"Hello, world!"
    compressed_data = gzip_compress(data)
    decompressor.decompress(compressed_data)
    assert decompressor.unconsumed_tail == b""

def test_gzip_decompressor_flush():
    decompressor = GzipDecompressor()
    data = b"Hello, world!"
    compressed_data = gzip_compress(data)
    decompressor.decompress(compressed_data)
    flushed_data = decompressor.flush()
    assert flushed_data == b""
