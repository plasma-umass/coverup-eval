# file: typesystem/base.py:207-210
# asked: {"lines": [207, 208], "branches": []}
# gained: {"lines": [207, 208], "branches": []}

import pytest
from typesystem.base import ParseError, BaseError

def test_parse_error_inheritance():
    assert issubclass(ParseError, BaseError)

def test_parse_error_message():
    error_message = "An error occurred"
    error = ParseError(text=error_message)
    assert str(error) == error_message
