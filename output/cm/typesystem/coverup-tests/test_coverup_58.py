# file typesystem/tokenize/tokens.py:101-106
# lines [101, 102, 103, 105, 106]
# branches []

import pytest
from typesystem.tokenize.tokens import Token, ListToken

class MockToken(Token):
    def __init__(self, value, start_index, end_index):
        super().__init__(value, start_index, end_index)

    def _get_value(self):
        return 'mock_value'

@pytest.fixture
def mock_token():
    return MockToken('mock_value', 0, 10)

def test_list_token_get_value_and_get_child_token(mock_token):
    list_token = ListToken([mock_token, mock_token, mock_token], 0, 30)
    
    # Test _get_value
    values = list_token._get_value()
    assert values == ['mock_value', 'mock_value', 'mock_value']
    
    # Test _get_child_token
    child_token = list_token._get_child_token(1)
    assert isinstance(child_token, Token)
    assert child_token._get_value() == 'mock_value'
