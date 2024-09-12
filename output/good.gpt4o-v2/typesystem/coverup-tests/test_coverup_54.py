# file: typesystem/tokenize/tokens.py:24-26
# asked: {"lines": [24, 25, 26], "branches": []}
# gained: {"lines": [24, 25, 26], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

def test_token_string_property():
    token = Token(value="test", start_index=0, end_index=3, content="test content")
    assert token.string == "test"

    token = Token(value="test", start_index=5, end_index=10, content="1234567890abcdef")
    assert token.string == "67890a"

    token = Token(value="test", start_index=0, end_index=0, content="a")
    assert token.string == "a"

    token = Token(value="test", start_index=1, end_index=1, content="ab")
    assert token.string == "b"
