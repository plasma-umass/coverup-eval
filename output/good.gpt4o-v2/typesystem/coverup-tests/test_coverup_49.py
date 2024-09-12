# file: typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [101, 102, 103, 105, 106], "branches": []}
# gained: {"lines": [101, 102, 103, 105, 106], "branches": []}

import pytest
from typesystem.tokenize.tokens import ListToken, Token

class MockToken(Token):
    def __init__(self):
        super().__init__(value="mock", start_index=0, end_index=1)
    
    def _get_value(self):
        return "mock_value"

def test_list_token_get_value():
    mock_tokens = [MockToken(), MockToken()]
    list_token = ListToken(value=mock_tokens, start_index=0, end_index=2)
    list_token._value = mock_tokens
    
    result = list_token._get_value()
    
    assert result == ["mock_value", "mock_value"]

def test_list_token_get_child_token():
    mock_tokens = [MockToken(), MockToken()]
    list_token = ListToken(value=mock_tokens, start_index=0, end_index=2)
    list_token._value = mock_tokens
    
    result = list_token._get_child_token(1)
    
    assert result == mock_tokens[1]
