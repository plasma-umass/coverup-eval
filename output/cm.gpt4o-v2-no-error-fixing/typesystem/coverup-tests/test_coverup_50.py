# file: typesystem/tokenize/tokens.py:49-54
# asked: {"lines": [53, 54], "branches": []}
# gained: {"lines": [53, 54], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self, children=None):
        self.children = children or {}

    def _get_child_token(self, key):
        return self.children.get(key, MockToken())

    def _get_key_token(self, key):
        return self.children.get(key, MockToken())

    def lookup(self, index: list) -> 'Token':
        token = self
        for key in index:
            token = token._get_child_token(key)
        return token

def test_lookup_key():
    # Setup
    child_token = MockToken()
    parent_token = MockToken(children={'a': child_token})

    # Test
    result = parent_token.lookup_key(['a'])

    # Assert
    assert result is child_token

    # Cleanup
    del parent_token
    del child_token

