# file docstring_parser/common.py:18-21
# lines [18, 19, 21]
# branches []

import pytest
from docstring_parser.common import ParseError

def test_parse_error():
    with pytest.raises(ParseError) as exc_info:
        raise ParseError("Test parse error")

    assert str(exc_info.value) == "Test parse error", "ParseError did not contain the correct message"
