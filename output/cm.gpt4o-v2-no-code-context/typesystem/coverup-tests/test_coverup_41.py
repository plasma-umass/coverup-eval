# file: typesystem/tokenize/tokens.py:15-16
# asked: {"lines": [15, 16], "branches": []}
# gained: {"lines": [15, 16], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self):
        pass

def test_token_get_value_raises_not_implemented_error():
    token = MockToken()
    with pytest.raises(NotImplementedError):
        token._get_value()
