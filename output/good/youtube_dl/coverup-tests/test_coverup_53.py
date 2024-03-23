# file youtube_dl/aes.py:281-282
# lines [282]
# branches []

import pytest
from youtube_dl.aes import sub_bytes

def test_sub_bytes():
    # Test data that covers all branches of the sub_bytes function
    test_data = [0x00, 0x10, 0x20, 0x30, 0x40, 0x50, 0x60, 0x70, 0x80, 0x90, 0xA0, 0xB0, 0xC0, 0xD0, 0xE0, 0xF0]
    expected_output = [sub_bytes([x])[0] for x in test_data]

    # Call the function with the test data
    output = sub_bytes(test_data)

    # Assert that the output is as expected
    assert output == expected_output, "The sub_bytes function did not return the expected output."

    # Clean up is not necessary as the test does not have any side effects
