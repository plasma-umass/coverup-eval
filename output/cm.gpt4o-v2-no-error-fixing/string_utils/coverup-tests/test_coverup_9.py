# file: string_utils/manipulation.py:213-217
# asked: {"lines": [213, 214, 215, 217], "branches": [[214, 215], [214, 217]]}
# gained: {"lines": [213, 214, 215, 217], "branches": [[214, 215], [214, 217]]}

import pytest
from string_utils.manipulation import __StringFormatter
from string_utils.errors import InvalidInputError

def test_string_formatter_with_valid_string():
    formatter = __StringFormatter("valid string")
    assert formatter.input_string == "valid string"

def test_string_formatter_with_invalid_input():
    with pytest.raises(InvalidInputError) as exc_info:
        __StringFormatter(123)
    assert str(exc_info.value) == 'Expected "str", received "int"'
