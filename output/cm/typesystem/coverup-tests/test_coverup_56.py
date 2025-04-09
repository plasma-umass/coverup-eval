# file typesystem/tokenize/tokens.py:28-30
# lines [28, 29, 30]
# branches []

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self):
        self._value = "mock_value"
        self.start_index = 0
        self.end_index = 10

    def _get_value(self):
        return self._value

@pytest.fixture
def mock_token():
    return MockToken()

def test_token_value(mock_token):
    assert mock_token.value == "mock_value"
