# file typesystem/tokenize/tokens.py:28-30
# lines [28, 29, 30]
# branches []

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self, value, start_index, end_index):
        self._value = value
        self.start_index = start_index
        self.end_index = end_index

    def _get_value(self):
        return self._value

def test_token_value_property():
    token = MockToken(value="mock_value", start_index=0, end_index=1)
    assert token.value == "mock_value"
