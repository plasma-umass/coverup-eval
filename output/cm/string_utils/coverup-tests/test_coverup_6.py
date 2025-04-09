# file string_utils/manipulation.py:161-170
# lines [161, 162, 163, 164, 166, 167, 169, 170]
# branches ['163->164', '163->166', '166->167', '166->169', '169->exit', '169->170']

import pytest
from string_utils.manipulation import __StringCompressor
from string_utils.errors import InvalidInputError

def is_string(value):
    return isinstance(value, str)

# Assuming the existence of the InvalidInputError class in the string_utils.errors module
# If it does not exist, it should be created or the correct exception should be used

def test_require_valid_input_and_encoding():
    # Test with valid input and encoding
    __StringCompressor._StringCompressor__require_valid_input_and_encoding("test", "utf-8")

    # Test with invalid input (not a string)
    with pytest.raises(InvalidInputError):
        __StringCompressor._StringCompressor__require_valid_input_and_encoding(123, "utf-8")

    # Test with empty input string
    with pytest.raises(ValueError) as exc_info:
        __StringCompressor._StringCompressor__require_valid_input_and_encoding("", "utf-8")
    assert str(exc_info.value) == 'Input string cannot be empty'

    # Test with invalid encoding (not a string)
    with pytest.raises(ValueError) as exc_info:
        __StringCompressor._StringCompressor__require_valid_input_and_encoding("test", 123)
    assert str(exc_info.value) == 'Invalid encoding'
