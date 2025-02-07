# file: string_utils/validation.py:116-138
# asked: {"lines": [116, 135, 136, 138], "branches": [[135, 136], [135, 138]]}
# gained: {"lines": [116, 135, 136, 138], "branches": [[135, 136], [135, 138]]}

import pytest
from string_utils.validation import is_number
from string_utils.errors import InvalidInputError

def test_is_number_with_valid_numbers():
    assert is_number('42') is True
    assert is_number('19.99') is True
    assert is_number('-9.12') is True
    assert is_number('1e3') is True

def test_is_number_with_invalid_numbers():
    assert is_number('1 2 3') is False
    assert is_number('abc') is False
    assert is_number('') is False

def test_is_number_with_non_string_input():
    with pytest.raises(InvalidInputError) as excinfo:
        is_number(123)
    assert str(excinfo.value) == 'Expected "str", received "int"'

    with pytest.raises(InvalidInputError) as excinfo:
        is_number(None)
    assert str(excinfo.value) == 'Expected "str", received "NoneType"'

    with pytest.raises(InvalidInputError) as excinfo:
        is_number(45.67)
    assert str(excinfo.value) == 'Expected "str", received "float"'
