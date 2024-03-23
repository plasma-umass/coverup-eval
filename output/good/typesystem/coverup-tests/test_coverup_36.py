# file typesystem/tokenize/tokens.py:66-71
# lines [66, 67, 68, 69, 70]
# branches []

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def _get_value(self):
        return "mock_value"

    def __init__(self, start_index, end_index):
        self._start_index = start_index
        self._end_index = end_index

@pytest.fixture
def token():
    return MockToken(start_index=0, end_index=10)

def test_token_eq(token):
    same_token = MockToken(start_index=0, end_index=10)
    different_token = MockToken(start_index=5, end_index=15)
    non_token = "not_a_token"

    assert token == same_token, "Tokens with the same value and indices should be equal"
    assert not (token == different_token), "Tokens with different indices should not be equal"
    assert not (token == non_token), "Token should not be equal to a non-token object"
