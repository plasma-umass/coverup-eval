# file typesystem/tokenize/tokens.py:63-64
# lines [63, 64]
# branches []

import pytest
from typesystem.tokenize.tokens import Token

def test_token_repr():
    class TestToken(Token):
        def __init__(self, string):
            self._string = string

        @property
        def string(self):
            return self._string

    token = TestToken("test_string")
    assert repr(token) == "TestToken('test_string')"
