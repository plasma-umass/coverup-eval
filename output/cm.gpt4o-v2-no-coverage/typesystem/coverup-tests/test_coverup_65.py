# file: typesystem/tokenize/tokens.py:28-30
# asked: {"lines": [28, 29, 30], "branches": []}
# gained: {"lines": [28, 29, 30], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

class TestToken(Token):
    def _get_value(self):
        return "test_value"

def test_token_value():
    token = TestToken("value", 0, 1)
    assert token.value == "test_value"

def test_token_value_not_implemented():
    token = Token("value", 0, 1)
    with pytest.raises(NotImplementedError):
        _ = token.value
