# file typesystem/tokenize/tokens.py:18-19
# lines [18, 19]
# branches []

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self):
        pass

class TestToken:
    def test_get_child_token(self):
        token = MockToken()
        with pytest.raises(NotImplementedError):
            token._get_child_token('any_key')
