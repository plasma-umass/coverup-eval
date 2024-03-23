# file typesystem/tokenize/tokens.py:15-16
# lines [15, 16]
# branches []

import pytest
from typesystem.tokenize.tokens import Token

class DummyToken(Token):
    def __init__(self):
        pass

class TestToken:
    def test_get_value_not_implemented(self):
        dummy_token = DummyToken()
        with pytest.raises(NotImplementedError):
            dummy_token._get_value()
