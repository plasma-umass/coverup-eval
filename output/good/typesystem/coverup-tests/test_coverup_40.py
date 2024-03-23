# file typesystem/tokenize/tokens.py:40-47
# lines [40, 44, 45, 46, 47]
# branches ['45->46', '45->47']

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_child_token(self, key):
        return self

    def _get_value(self):
        return None

@pytest.fixture
def mock_token():
    return MockToken(value=None, start_index=0, end_index=0)

def test_lookup(mock_token):
    index = [1, 2, 3]
    result = mock_token.lookup(index)
    assert result == mock_token
