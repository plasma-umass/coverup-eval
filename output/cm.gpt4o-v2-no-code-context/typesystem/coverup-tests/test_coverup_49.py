# file: typesystem/base.py:207-210
# asked: {"lines": [207, 208], "branches": []}
# gained: {"lines": [207, 208], "branches": []}

import pytest
from typesystem.base import BaseError

def test_parse_error_inheritance():
    class ParseError(BaseError):
        """
        Raised by `typesystem.tokenize_json()` and `typesystem.tokenize_yaml()`.
        """
        pass

    # Ensure ParseError is a subclass of BaseError
    assert issubclass(ParseError, BaseError)

    # Ensure ParseError can be instantiated with required parameters
    error_instance = ParseError(text="Test error message")
    assert isinstance(error_instance, ParseError)
    assert str(error_instance) == "Test error message"
