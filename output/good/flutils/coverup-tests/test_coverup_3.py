# file flutils/codecs/b64.py:17-62
# lines [17, 19, 36, 39, 40, 41, 42, 43, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58, 59, 62]
# branches []

import pytest
import base64
from flutils.codecs.b64 import encode
from collections import UserString

def test_encode_with_userstring():
    # Create a UserString instance with base64 encoded data
    user_string = UserString('SGVsbG8gV29ybGQh')
    
    # Expected output
    expected_output = b'Hello World!'
    
    # Call the encode function with the UserString instance
    result, length = encode(user_string)
    
    # Assert that the output is as expected
    assert result == expected_output
    assert length == len(user_string)

def test_encode_with_invalid_base64_userstring():
    # Create a UserString instance with invalid base64 data
    user_string = UserString('Invalid base64 data')
    
    # Call the encode function and expect a UnicodeEncodeError
    with pytest.raises(UnicodeEncodeError) as exc_info:
        encode(user_string)
    
    # Assert that the exception message contains the expected text
    assert 'is not a proper bas64 character string' in str(exc_info.value)
