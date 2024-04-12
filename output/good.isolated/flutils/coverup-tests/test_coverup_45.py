# file flutils/codecs/raw_utf8_escape.py:91-140
# lines [91, 93, 114, 117, 123, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 140]
# branches []

import pytest
from flutils.codecs.raw_utf8_escape import decode

def test_decode_with_invalid_utf8_sequence():
    # Prepare a byte string with an invalid utf8 sequence
    invalid_utf8_sequence = b'Invalid sequence: \\xff'
    
    # Expect a UnicodeDecodeError to be raised
    with pytest.raises(UnicodeDecodeError) as exc_info:
        decode(invalid_utf8_sequence)
    
    # Assert that the exception has the correct attributes
    assert exc_info.value.encoding == 'eutf8h'
    assert exc_info.value.object == invalid_utf8_sequence
    assert exc_info.value.start == 18  # Corrected start index
    assert exc_info.value.end == 19
    assert 'invalid start byte' in exc_info.value.reason

def test_decode_with_valid_utf8_sequence():
    # Prepare a byte string with a valid utf8 sequence
    valid_utf8_sequence = b'Valid sequence: \\xc3\\xa9'  # é in utf8
    
    # Decode the sequence
    result, consumed = decode(valid_utf8_sequence)
    
    # Assert the result is correct and all bytes were consumed
    assert result == 'Valid sequence: é'
    assert consumed == len(valid_utf8_sequence)
