# file: string_utils/manipulation.py:213-217
# asked: {"lines": [213, 214, 215, 217], "branches": [[214, 215], [214, 217]]}
# gained: {"lines": [213, 214, 215, 217], "branches": [[214, 215], [214, 217]]}

import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError
from string_utils.validation import is_string

def test_string_formatter_initialization_with_valid_string():
    formatter = __StringFormatter("valid_string")
    assert formatter.input_string == "valid_string"

def test_string_formatter_initialization_with_invalid_string():
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)

def test_string_formatter_initialization_with_empty_string():
    formatter = __StringFormatter("")
    assert formatter.input_string == ""

def test_string_formatter_initialization_with_none(monkeypatch):
    monkeypatch.setattr('string_utils.validation.is_string', lambda x: False)
    with pytest.raises(InvalidInputError):
        __StringFormatter(None)
