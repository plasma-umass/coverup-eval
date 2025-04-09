# file: typesystem/tokenize/tokens.py:56-61
# asked: {"lines": [57, 58, 59, 60, 61], "branches": []}
# gained: {"lines": [57, 58, 59, 60, 61], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token
from typesystem.base import Position

class TestToken:
    @pytest.fixture
    def token(self):
        class MockToken(Token):
            def __init__(self, content):
                self._content = content

        return MockToken

    def test_get_position_single_line(self, token):
        t = token("hello")
        position = t._get_position(4)
        assert position == Position(1, 5, 4)

    def test_get_position_multiple_lines(self, token):
        t = token("hello\nworld")
        position = t._get_position(10)
        assert position == Position(2, 5, 10)

    def test_get_position_empty_content(self, token):
        t = token("")
        position = t._get_position(0)
        assert position == Position(1, 1, 0)

    def test_get_position_newline_at_end(self, token):
        t = token("hello\n")
        position = t._get_position(5)
        assert position == Position(1, 5, 5)
