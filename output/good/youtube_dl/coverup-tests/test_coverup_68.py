# file youtube_dl/socks.py:134-136
# lines [136]
# branches []

import pytest
from youtube_dl.socks import sockssocket
from youtube_dl.compat import compat_struct_pack

def test_len_and_data():
    # Test data
    test_data = b'test_data'
    expected_length = len(test_data)
    expected_packed_length = compat_struct_pack('!B', expected_length)

    # Call the static method
    result = sockssocket._len_and_data(test_data)

    # Assertions to verify postconditions
    assert result[:1] == expected_packed_length, "Packed length does not match expected value"
    assert result[1:] == test_data, "Data does not match expected value"

    # No cleanup necessary as no external resources or state changes are involved
