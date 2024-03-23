# file httpie/core.py:234-247
# lines [234, 243, 244, 245, 246]
# branches []

import pytest
from httpie.core import decode_raw_args

def test_decode_raw_args_with_mixed_types(mocker):
    # Mock the stdin encoding
    stdin_encoding = 'utf-8'
    mocker.patch('sys.stdin', mocker.Mock(encoding=stdin_encoding))

    # Prepare the input with mixed types: str and bytes
    input_args = ['arg1', b'arg2', 'arg3', b'arg4']

    # Expected output should have all strings
    expected_output = ['arg1', 'arg2', 'arg3', 'arg4']

    # Call the function to test
    result = decode_raw_args(input_args, stdin_encoding)

    # Assert that the result matches the expected output
    assert result == expected_output, "The decoded arguments do not match the expected output."

    # No cleanup is necessary as we are not modifying any global state
