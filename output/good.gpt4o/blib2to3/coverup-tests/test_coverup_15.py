# file src/blib2to3/pgen2/parse.py:42-54
# lines [42, 43, 45, 48, 49, 51, 52, 53, 54]
# branches []

import pytest
from blib2to3.pgen2.parse import ParseError

def test_parse_error():
    # Arrange
    msg = "Parser is stuck"
    type = 1
    value = "some_value"
    context = "some_context"
    
    # Act
    error = ParseError(msg, type, value, context)
    
    # Assert
    assert error.msg == msg
    assert error.type == type
    assert error.value == value
    assert error.context == context
    assert str(error) == f"{msg}: type={type!r}, value={value!r}, context={context!r}"
