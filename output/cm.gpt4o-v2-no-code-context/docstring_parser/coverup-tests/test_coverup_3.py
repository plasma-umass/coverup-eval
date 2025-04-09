# file: docstring_parser/common.py:18-21
# asked: {"lines": [18, 19, 21], "branches": []}
# gained: {"lines": [18, 19, 21], "branches": []}

import pytest
from docstring_parser.common import ParseError

def test_parse_error_inheritance():
    assert issubclass(ParseError, RuntimeError)

def test_parse_error_instance():
    error_instance = ParseError("Test error message")
    assert isinstance(error_instance, ParseError)
    assert str(error_instance) == "Test error message"
