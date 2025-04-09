# file: string_utils/validation.py:116-138
# asked: {"lines": [116, 135, 136, 138], "branches": [[135, 136], [135, 138]]}
# gained: {"lines": [116, 135, 136, 138], "branches": [[135, 136], [135, 138]]}

import pytest
from string_utils.validation import is_number
from string_utils.errors import InvalidInputError
import re

# Mocking NUMBER_RE for testing purposes
NUMBER_RE = re.compile(r'^[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$')

def test_is_number_valid_numbers(monkeypatch):
    monkeypatch.setattr('string_utils.validation.NUMBER_RE', NUMBER_RE)
    assert is_number('42') is True
    assert is_number('19.99') is True
    assert is_number('-9.12') is True
    assert is_number('1e3') is True

def test_is_number_invalid_numbers(monkeypatch):
    monkeypatch.setattr('string_utils.validation.NUMBER_RE', NUMBER_RE)
    assert is_number('1 2 3') is False
    assert is_number('abc') is False
    assert is_number('') is False
    assert is_number('1.2.3') is False
    assert is_number('1e') is False

def test_is_number_invalid_input_type():
    with pytest.raises(InvalidInputError) as excinfo:
        is_number(123)
    assert str(excinfo.value) == 'Expected "str", received "int"'

    with pytest.raises(InvalidInputError) as excinfo:
        is_number(None)
    assert str(excinfo.value) == 'Expected "str", received "NoneType"'

    with pytest.raises(InvalidInputError) as excinfo:
        is_number([])
    assert str(excinfo.value) == 'Expected "str", received "list"'
