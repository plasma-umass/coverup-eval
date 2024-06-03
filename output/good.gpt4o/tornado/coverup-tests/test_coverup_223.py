# file tornado/util.py:90-128
# lines [101, 114, 120, 128]
# branches []

import pytest
import zlib
from tornado.util import GzipDecompressor

def test_gzip_decompressor(mocker):
    # Mocking zlib.decompressobj to ensure we can control its behavior
    mock_decompressobj = mocker.patch('zlib.decompressobj')
    mock_instance = mock_decompressobj.return_value

    # Mocking the return values for the methods
    mock_instance.decompress.return_value = b'decompressed_data'
    mock_instance.unconsumed_tail = b'unconsumed_data'
    mock_instance.flush.return_value = b'flushed_data'

    decompressor = GzipDecompressor()

    # Test the __init__ method (line 101)
    mock_decompressobj.assert_called_once_with(16 + zlib.MAX_WBITS)

    # Test the decompress method (line 114)
    result = decompressor.decompress(b'compressed_data', max_length=10)
    mock_instance.decompress.assert_called_once_with(b'compressed_data', 10)
    assert result == b'decompressed_data'

    # Test the unconsumed_tail property (line 120)
    result = decompressor.unconsumed_tail
    assert result == b'unconsumed_data'

    # Test the flush method (line 128)
    result = decompressor.flush()
    mock_instance.flush.assert_called_once()
    assert result == b'flushed_data'
