# file: typesystem/tokenize/tokens.py:74-79
# asked: {"lines": [74, 75, 76, 78, 79], "branches": []}
# gained: {"lines": [74, 75, 76, 78, 79], "branches": []}

import pytest
from typesystem.tokenize.tokens import ScalarToken

class MockToken:
    def __init__(self, value):
        self._value = value

@pytest.fixture
def mock_scalar_token():
    return MockToken(value="test_value")

def test_scalar_token_hash(mock_scalar_token):
    token = ScalarToken.__new__(ScalarToken)
    token._value = mock_scalar_token._value
    assert token.__hash__() == hash("test_value")

def test_scalar_token_get_value(mock_scalar_token):
    token = ScalarToken.__new__(ScalarToken)
    token._value = mock_scalar_token._value
    assert token._get_value() == "test_value"
