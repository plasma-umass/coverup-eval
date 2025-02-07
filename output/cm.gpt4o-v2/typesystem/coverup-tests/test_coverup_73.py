# file: typesystem/tokenize/tokens.py:63-64
# asked: {"lines": [63, 64], "branches": []}
# gained: {"lines": [63, 64], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

def test_token_repr():
    token = Token(value="test", start_index=0, end_index=10, content="test content")
    repr_str = repr(token)
    assert repr_str == "Token('test conten')"
