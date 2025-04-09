# file typesystem/tokenize/tokens.py:63-64
# lines [63, 64]
# branches []

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self, string):
        self._string = string

    @property
    def string(self):
        return self._string

@pytest.fixture
def mock_token():
    return MockToken("test_string")

def test_token_repr(mock_token):
    assert repr(mock_token) == "MockToken('test_string')"
