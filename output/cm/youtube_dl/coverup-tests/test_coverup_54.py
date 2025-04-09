# file youtube_dl/aes.py:301-302
# lines [302]
# branches []

import pytest
from youtube_dl.aes import xor

def test_xor():
    # Test data
    data1 = [0x01, 0x02, 0x03]
    data2 = [0x01, 0x02, 0x03]
    expected_result = [0x00, 0x00, 0x00]  # XOR of two identical lists should result in a list of zeros

    # Perform the XOR operation
    result = xor(data1, data2)

    # Assert that the result is as expected
    assert result == expected_result, "XOR operation did not produce the expected result"

    # Test with different data to ensure line 302 is executed with different bytes
    data1 = [0x01, 0xFF, 0x00]
    data2 = [0xFF, 0x01, 0xAA]
    expected_result = [0xFE, 0xFE, 0xAA]  # Expected result of XOR operation

    # Perform the XOR operation
    result = xor(data1, data2)

    # Assert that the result is as expected
    assert result == expected_result, "XOR operation did not produce the expected result"
