# file: typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [40, 44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [40, 44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self, value, start_index, end_index, content='', children=None):
        super().__init__(value, start_index, end_index, content)
        self.children = children or {}
        self._value = value

    def _get_child_token(self, key):
        return self.children.get(key, None)

    def _get_value(self):
        return self._value

def test_token_lookup():
    # Create a mock token structure
    grandchild_token = MockToken(value='grandchild', start_index=2, end_index=3)
    child_token = MockToken(value='child', start_index=1, end_index=2, children={'grandchild': grandchild_token})
    root_token = MockToken(value='root', start_index=0, end_index=1, children={'child': child_token})

    # Test lookup for a nested token
    result = root_token.lookup(['child', 'grandchild'])
    assert result == grandchild_token

    # Test lookup for a direct child token
    result = root_token.lookup(['child'])
    assert result == child_token

    # Test lookup for a non-existent token
    result = root_token.lookup(['nonexistent'])
    assert result is None

    # Test lookup for a non-existent nested token
    result = root_token.lookup(['child', 'nonexistent'])
    assert result is None
