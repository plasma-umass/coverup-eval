# file: typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [103, 106], "branches": []}
# gained: {"lines": [103, 106], "branches": []}

import pytest
from typesystem.tokenize.tokens import ListToken, Token

class MockToken(Token):
    def __init__(self, value, start_index=0, end_index=0):
        self._value = value
        self.start_index = start_index
        self.end_index = end_index

    def _get_value(self):
        return self._value

@pytest.fixture
def list_token():
    return ListToken([MockToken(1), MockToken(2), MockToken(3)], start_index=0, end_index=3)

def test_get_value(list_token):
    result = list_token._get_value()
    assert result == [1, 2, 3]

def test_get_child_token(list_token):
    child_token = list_token._get_child_token(1)
    assert isinstance(child_token, MockToken)
    assert child_token._get_value() == 2
