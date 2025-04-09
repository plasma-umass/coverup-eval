# file: typesystem/tokenize/tokens.py:7-13
# asked: {"lines": [7, 8, 10, 11, 12, 13], "branches": []}
# gained: {"lines": [7, 8, 10, 11, 12, 13], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

@pytest.fixture
def token():
    return Token(value="test", start_index=0, end_index=4, content="test content")

def test_token_initialization(token):
    assert token._value == "test"
    assert token._start_index == 0
    assert token._end_index == 4
    assert token._content == "test content"

def test_token_initialization_without_content():
    token = Token(value="test", start_index=0, end_index=4)
    assert token._value == "test"
    assert token._start_index == 0
    assert token._end_index == 4
    assert token._content == ""
