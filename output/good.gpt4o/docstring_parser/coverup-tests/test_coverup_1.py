# file docstring_parser/common.py:18-21
# lines [18, 19, 21]
# branches []

import pytest
from docstring_parser.common import ParseError

def test_parse_error():
    with pytest.raises(ParseError):
        raise ParseError("This is a parsing error")

    error_instance = ParseError("Another parsing error")
    assert isinstance(error_instance, ParseError)
    assert str(error_instance) == "Another parsing error"
