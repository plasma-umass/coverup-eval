# file: typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self, children=None):
        self.children = children or {}

    def _get_child_token(self, key):
        return self.children.get(key, None)

def test_token_lookup():
    # Setup
    child_token_2 = MockToken()
    child_token_1 = MockToken(children={2: child_token_2})
    root_token = MockToken(children={1: child_token_1})

    # Test
    result = root_token.lookup([1, 2])

    # Assert
    assert result is child_token_2

def test_token_lookup_nonexistent_key():
    # Setup
    child_token_1 = MockToken()
    root_token = MockToken(children={1: child_token_1})

    # Test
    result = root_token.lookup([1, 2])

    # Assert
    assert result is None

def test_token_lookup_empty_index():
    # Setup
    root_token = MockToken()

    # Test
    result = root_token.lookup([])

    # Assert
    assert result is root_token
