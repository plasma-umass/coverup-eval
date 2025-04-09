# file typesystem/tokenize/tokens.py:56-61
# lines [56, 57, 58, 59, 60, 61]
# branches []

import pytest
from typesystem.tokenize.tokens import Token, Position

@pytest.fixture
def token():
    class MockToken(Token):
        def __init__(self, content):
            self._content = content

    return MockToken

def test_get_position(token):
    # Test with content having multiple lines
    t = token("line1\nline2\nline3")
    pos = t._get_position(10)
    assert pos.line_no == 2
    assert pos.column_no == 5
    assert pos.char_index == 10

    # Test with content having a single line
    t = token("singleline")
    pos = t._get_position(5)
    assert pos.line_no == 1
    assert pos.column_no == 6
    assert pos.char_index == 5

    # Test with empty content
    t = token("")
    pos = t._get_position(0)
    assert pos.line_no == 1
    assert pos.column_no == 1
    assert pos.char_index == 0

    # Test with content having a single character
    t = token("a")
    pos = t._get_position(0)
    assert pos.line_no == 1
    assert pos.column_no == 1
    assert pos.char_index == 0
