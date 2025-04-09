# file: typesystem/tokenize/tokens.py:63-64
# asked: {"lines": [63, 64], "branches": []}
# gained: {"lines": [63, 64], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

def test_token_repr():
    token = Token(value="test", start_index=0, end_index=4, content="test content")
    expected_repr = "Token('test ')"
    assert repr(token) == expected_repr
