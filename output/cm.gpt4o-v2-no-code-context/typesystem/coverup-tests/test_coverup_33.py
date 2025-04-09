# file: typesystem/tokenize/tokens.py:56-61
# asked: {"lines": [56, 57, 58, 59, 60, 61], "branches": []}
# gained: {"lines": [56, 57, 58, 59, 60, 61], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token, Position

@pytest.fixture
def token():
    class MockToken(Token):
        def __init__(self, content):
            self._content = content

    return MockToken

def test_get_position_single_line(token):
    t = token("Hello, world!")
    pos = t._get_position(5)
    assert pos.line_no == 1
    assert pos.column_no == 6

def test_get_position_multi_line(token):
    t = token("Hello,\nworld!")
    pos = t._get_position(7)
    assert pos.line_no == 2
    assert pos.column_no == 1

def test_get_position_empty_content(token):
    t = token("")
    pos = t._get_position(0)
    assert pos.line_no == 1
    assert pos.column_no == 1

def test_get_position_end_of_content(token):
    t = token("Hello,\nworld!")
    pos = t._get_position(12)
    assert pos.line_no == 2
    assert pos.column_no == 6
