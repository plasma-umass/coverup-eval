# file typesystem/tokenize/tokens.py:32-34
# lines [32, 33, 34]
# branches []

import pytest
from typesystem.tokenize.tokens import Token

class MockPosition:
    def __init__(self, line, column):
        self.line = line
        self.column = column

class MockToken(Token):
    def __init__(self, start_index):
        self._start_index = start_index

    def _get_position(self, index):
        return MockPosition(line=index, column=index)

def test_token_start_property():
    token = MockToken(start_index=5)
    start_position = token.start
    assert isinstance(start_position, MockPosition)
    assert start_position.line == 5
    assert start_position.column == 5
