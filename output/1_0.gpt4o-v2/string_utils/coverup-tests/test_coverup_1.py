# file: string_utils/errors.py:6-17
# asked: {"lines": [6, 7, 11, 15, 16, 17], "branches": []}
# gained: {"lines": [6, 7, 11, 15, 16, 17], "branches": []}

import pytest
from string_utils.errors import InvalidInputError

def test_invalid_input_error_with_int():
    with pytest.raises(InvalidInputError) as exc_info:
        raise InvalidInputError(123)
    assert str(exc_info.value) == 'Expected "str", received "int"'

def test_invalid_input_error_with_list():
    with pytest.raises(InvalidInputError) as exc_info:
        raise InvalidInputError([1, 2, 3])
    assert str(exc_info.value) == 'Expected "str", received "list"'

def test_invalid_input_error_with_dict():
    with pytest.raises(InvalidInputError) as exc_info:
        raise InvalidInputError({'key': 'value'})
    assert str(exc_info.value) == 'Expected "str", received "dict"'

def test_invalid_input_error_with_none():
    with pytest.raises(InvalidInputError) as exc_info:
        raise InvalidInputError(None)
    assert str(exc_info.value) == 'Expected "str", received "NoneType"'
