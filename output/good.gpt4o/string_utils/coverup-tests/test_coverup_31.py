# file string_utils/validation.py:116-138
# lines [116, 135, 136, 138]
# branches ['135->136', '135->138']

import pytest
import re
from string_utils.validation import is_number, InvalidInputError

def test_is_number_valid_cases():
    assert is_number('42') is True
    assert is_number('19.99') is True
    assert is_number('-9.12') is True
    assert is_number('1e3') is True

def test_is_number_invalid_cases():
    assert is_number('1 2 3') is False
    assert is_number('abc') is False
    assert is_number('') is False

def test_is_number_invalid_input_type():
    with pytest.raises(InvalidInputError):
        is_number(123)
    with pytest.raises(InvalidInputError):
        is_number(None)
    with pytest.raises(InvalidInputError):
        is_number([])

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Mocking NUMBER_RE to ensure it is defined and used correctly
    mocker.patch('string_utils.validation.NUMBER_RE', new_callable=lambda: re.compile(r'^[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$'))
