# file: typesystem/tokenize/tokens.py:49-54
# asked: {"lines": [53, 54], "branches": []}
# gained: {"lines": [53, 54], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self, children=None):
        self.children = children or {}

    def _get_child_token(self, key):
        return self.children.get(key, None)

    def _get_key_token(self, key):
        return self.children.get(key, None)

    def lookup(self, index: list) -> 'Token':
        token = self
        for key in index:
            token = token._get_child_token(key)
        return token

def test_lookup_key():
    # Setup
    key_token = MockToken()
    child_token = MockToken(children={'key': key_token})
    root_token = MockToken(children={'child': child_token})

    # Execute
    result = root_token.lookup_key(['child', 'key'])

    # Verify
    assert result is key_token

    # Cleanup
    del key_token
    del child_token
    del root_token
