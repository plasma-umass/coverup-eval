# file: typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [101, 102, 103, 105, 106], "branches": []}
# gained: {"lines": [101, 102, 103, 105, 106], "branches": []}

import pytest
from typesystem.tokenize.tokens import ListToken, Token

class MockToken(Token):
    def _get_value(self):
        return "mock_value"

def test_list_token_get_value():
    tokens = [MockToken("value1", 0, 1), MockToken("value2", 1, 2)]
    list_token = ListToken(tokens, 0, 2)
    assert list_token._get_value() == ["mock_value", "mock_value"]

def test_list_token_get_child_token():
    tokens = [MockToken("value1", 0, 1), MockToken("value2", 1, 2)]
    list_token = ListToken(tokens, 0, 2)
    assert list_token._get_child_token(0) == tokens[0]
    assert list_token._get_child_token(1) == tokens[1]
