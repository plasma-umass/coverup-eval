# file: httpie/cli/exceptions.py:1-2
# asked: {"lines": [1, 2], "branches": []}
# gained: {"lines": [1, 2], "branches": []}

import pytest
from httpie.cli.exceptions import ParseError

def test_parse_error():
    with pytest.raises(ParseError):
        raise ParseError("This is a parse error")
