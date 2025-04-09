# file typesystem/tokenize/tokens.py:21-22
# lines [21, 22]
# branches []

import pytest
from typesystem.tokenize.tokens import Token

class DummyToken(Token):
    def __init__(self):
        pass

class TestToken:
    def test_get_key_token_not_implemented(self):
        token = DummyToken()
        with pytest.raises(NotImplementedError):
            token._get_key_token("test_key")
