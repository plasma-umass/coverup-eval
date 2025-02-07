# file: typesystem/tokenize/tokens.py:28-30
# asked: {"lines": [28, 29, 30], "branches": []}
# gained: {"lines": [28, 29, 30], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def _get_value(self):
        return "mock_value"

def test_token_value_property():
    token = MockToken(value="test", start_index=0, end_index=4)
    assert token.value == "mock_value"
