# file: src/blib2to3/pgen2/parse.py:42-54
# asked: {"lines": [48, 49, 51, 52, 53, 54], "branches": []}
# gained: {"lines": [48, 49, 51, 52, 53, 54], "branches": []}

import pytest
from blib2to3.pytree import Context
from blib2to3.pgen2.parse import ParseError

def test_parse_error_initialization():
    msg = "Error message"
    type = 1
    value = "Some value"
    context = ("Some context", (1, 2))

    error = ParseError(msg, type, value, context)

    assert error.msg == msg
    assert error.type == type
    assert error.value == value
    assert error.context == context
    assert str(error) == "Error message: type=1, value='Some value', context=('Some context', (1, 2))"
