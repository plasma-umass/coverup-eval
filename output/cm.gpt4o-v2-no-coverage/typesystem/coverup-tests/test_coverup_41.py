# file: typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [101, 102, 103, 105, 106], "branches": []}
# gained: {"lines": [101, 102, 103, 105, 106], "branches": []}

import pytest
from typesystem.tokenize.tokens import ListToken, Token

class MockToken(Token):
    def __init__(self, value):
        super().__init__(value, 0, 0)

    def _get_value(self):
        return self._value

@pytest.fixture
def mock_token_list():
    return ListToken([MockToken(1), MockToken(2), MockToken(3)], 0, 0)

def test_get_value(mock_token_list):
    result = mock_token_list._get_value()
    assert result == [1, 2, 3]

def test_get_child_token(mock_token_list):
    child_token = mock_token_list._get_child_token(1)
    assert isinstance(child_token, MockToken)
    assert child_token._get_value() == 2
