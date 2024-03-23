# file flutils/codecs/b64.py:66-92
# lines [66, 68, 84, 87, 90, 92]
# branches []

import pytest
from flutils.codecs.b64 import decode

def test_decode():
    # Test with bytes
    data_bytes = b'test data'
    expected_str = 'dGVzdCBkYXRh'
    result_str, consumed = decode(data_bytes)
    assert result_str == expected_str
    assert consumed == len(data_bytes)

    # Test with bytearray
    data_bytearray = bytearray(data_bytes)
    result_str, consumed = decode(data_bytearray)
    assert result_str == expected_str
    assert consumed == len(data_bytearray)

    # Test with memoryview
    data_memoryview = memoryview(data_bytes)
    result_str, consumed = decode(data_memoryview)
    assert result_str == expected_str
    assert consumed == len(data_memoryview)
