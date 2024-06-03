# file typesystem/tokenize/tokens.py:40-47
# lines [40, 44, 45, 46, 47]
# branches ['45->46', '45->47']

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self, children=None):
        self.children = children or {}

    def _get_child_token(self, key):
        return self.children.get(key, None)

def test_token_lookup():
    # Create a mock token structure
    grandchild_token = MockToken()
    child_token = MockToken(children={1: grandchild_token})
    root_token = MockToken(children={0: child_token})

    # Test lookup method
    result = root_token.lookup([0, 1])
    assert result is grandchild_token

    # Test lookup with non-existent key
    result = root_token.lookup([0, 2])
    assert result is None

    # Test lookup with empty index
    result = root_token.lookup([])
    assert result is root_token
