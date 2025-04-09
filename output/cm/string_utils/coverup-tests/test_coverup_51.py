# file string_utils/manipulation.py:213-217
# lines [215]
# branches ['214->215']

import pytest

# Assuming the InvalidInputError is defined within the same module for this context
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_string_formatter_with_invalid_input():
    with pytest.raises(InvalidInputError) as exc_info:
        __StringFormatter(123)  # Pass a non-string input to trigger the exception
    assert str(exc_info.value.args[0]) == 'Expected "str", received "int"'  # Corrected assertion
