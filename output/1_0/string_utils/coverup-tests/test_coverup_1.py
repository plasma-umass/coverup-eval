# file string_utils/errors.py:6-17
# lines [6, 7, 11, 15, 16, 17]
# branches []

import pytest
from string_utils.errors import InvalidInputError

def test_invalid_input_error():
    with pytest.raises(InvalidInputError) as exc_info:
        raise InvalidInputError(123)

    assert str(exc_info.value) == 'Expected "str", received "int"'
