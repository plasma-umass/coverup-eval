# file typesystem/tokenize/tokens.py:101-106
# lines [101, 102, 103, 105, 106]
# branches []

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
    tokens = [MockToken(1), MockToken(2), MockToken(3)]
    return ListToken(tokens, start_index=0, end_index=3)

def test_list_token_get_value(list_token):
    assert list_token._get_value() == [1, 2, 3]

def test_list_token_get_child_token(list_token):
    assert list_token._get_child_token(0)._get_value() == 1
    assert list_token._get_child_token(1)._get_value() == 2
    assert list_token._get_child_token(2)._get_value() == 3
