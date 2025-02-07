# file: typesystem/tokenize/tokens.py:32-34
# asked: {"lines": [32, 33, 34], "branches": []}
# gained: {"lines": [32, 33, 34], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token
from typesystem.base import Position

def test_token_start():
    token = Token(value="test", start_index=0, end_index=4, content="test content")
    start_position = token.start
    assert isinstance(start_position, Position)
    assert start_position.line_no == 1
    assert start_position.column_no == 1
    assert start_position.char_index == 0
