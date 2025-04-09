# file: docstring_parser/common.py:18-21
# asked: {"lines": [18, 19, 21], "branches": []}
# gained: {"lines": [18, 19, 21], "branches": []}

import pytest
from docstring_parser.common import ParseError

def test_parse_error_inheritance():
    with pytest.raises(ParseError):
        raise ParseError("This is a parse error")

    assert issubclass(ParseError, RuntimeError)
