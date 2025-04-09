# file: typesystem/tokenize/tokens.py:74-79
# asked: {"lines": [74, 75, 76, 78, 79], "branches": []}
# gained: {"lines": [74, 75, 76, 78, 79], "branches": []}

import pytest
from typesystem.tokenize.tokens import ScalarToken

class MockToken(ScalarToken):
    def __init__(self, value):
        self._value = value

@pytest.fixture
def mock_token():
    return MockToken(value="test_value")

def test_scalar_token_hash(mock_token):
    token = mock_token
    assert token.__hash__() == hash("test_value")

def test_scalar_token_get_value(mock_token):
    token = mock_token
    assert token._get_value() == "test_value"
