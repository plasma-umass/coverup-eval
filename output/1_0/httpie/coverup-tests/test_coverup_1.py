# file httpie/cli/exceptions.py:1-2
# lines [1, 2]
# branches []

import pytest
from httpie.cli.exceptions import ParseError

def test_parse_error():
    with pytest.raises(ParseError) as exc_info:
        raise ParseError("Test parse error")

    assert str(exc_info.value) == "Test parse error"
