# file string_utils/manipulation.py:213-217
# lines [213, 214, 215, 217]
# branches ['214->215', '214->217']

import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def is_string(value):
    return isinstance(value, str)

def test_string_formatter_with_invalid_input():
    with pytest.raises(InvalidInputError):
        __StringFormatter(123)  # Non-string input to trigger the exception

def test_string_formatter_with_valid_input():
    formatter = __StringFormatter("valid string")
    assert formatter.input_string == "valid string"

