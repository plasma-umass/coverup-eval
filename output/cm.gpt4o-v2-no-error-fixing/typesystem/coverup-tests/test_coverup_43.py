# file: typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [40, 44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [40, 44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self, value=None, start_index=0, end_index=0, content='', children=None):
        super().__init__(value, start_index, end_index, content)
        self.children = children or {}

    def _get_child_token(self, key):
        if key in self.children:
            return self.children[key]
        raise KeyError(f"Child token with key {key} not found")

def test_lookup_single_level():
    child_token = MockToken()
    parent_token = MockToken(children={'a': child_token})
    result = parent_token.lookup(['a'])
    assert result is child_token

def test_lookup_multiple_levels():
    grandchild_token = MockToken()
    child_token = MockToken(children={'b': grandchild_token})
    parent_token = MockToken(children={'a': child_token})
    result = parent_token.lookup(['a', 'b'])
    assert result is grandchild_token

def test_lookup_key_error():
    parent_token = MockToken(children={'a': MockToken()})
    with pytest.raises(KeyError):
        parent_token.lookup(['a', 'b'])
