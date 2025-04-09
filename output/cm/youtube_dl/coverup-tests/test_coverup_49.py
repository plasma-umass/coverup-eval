# file youtube_dl/swfinterp.py:100-111
# lines [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]
# branches ['103->104', '103->111', '108->109', '108->110']

import pytest
from youtube_dl.swfinterp import _read_int
from io import BytesIO

def test_read_int_full_coverage():
    # Test case to cover lines 101-111
    # Create a BytesIO object to simulate a reader that will require multiple iterations to read an int
    # The integer to read is 0x80 0x80 0x80 0x80 0x01, which is a continuation pattern that will cover all lines
    data = b'\x80\x80\x80\x80\x01'
    reader = BytesIO(data)

    # Call the function under test
    result = _read_int(reader)

    # Verify the result is correct
    # The expected result is calculated as follows:
    # (0x01 << 28) | (0x00 << 21) | (0x00 << 14) | (0x00 << 7) | 0x00
    expected_result = 0x10000000
    assert result == expected_result

    # Verify that the reader is at the end of the stream
    assert reader.read() == b''

    # Clean up
    reader.close()

# Run the test
def test_suite():
    test_read_int_full_coverage()

if __name__ == "__main__":
    pytest.main([__file__])
