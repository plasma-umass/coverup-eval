# file typesystem/tokenize/tokens.py:74-79
# lines [74, 75, 76, 78, 79]
# branches []

import pytest
from typesystem.tokenize.tokens import ScalarToken

class MockToken:
    def __init__(self, value):
        self._value = value

@pytest.fixture
def mock_token():
    return MockToken("test_value")

def test_scalar_token_hash(mock_token):
    scalar_token = ScalarToken(mock_token._value, 0, 1)
    assert hash(scalar_token) == hash("test_value")

def test_scalar_token_get_value(mock_token):
    scalar_token = ScalarToken(mock_token._value, 0, 1)
    assert scalar_token._get_value() == "test_value"
