# file: typesystem/tokenize/tokens.py:82-98
# asked: {"lines": [82, 83, 84, 85, 86, 88, 89, 90, 91, 94, 95, 97, 98], "branches": []}
# gained: {"lines": [82, 83, 84, 85, 86, 88, 89, 90, 91, 94, 95, 97, 98], "branches": []}

import pytest
from typesystem.tokenize.tokens import DictToken, Token

class MockToken(Token):
    def __init__(self, value, start_index=0, end_index=0, content=''):
        super().__init__(value, start_index, end_index, content)
    
    def _get_value(self):
        return self._value
    
    def __hash__(self):
        return hash(self._value)

def test_dict_token_initialization():
    key_token = MockToken("key", 0, 1)
    value_token = MockToken("value", 2, 5)
    dict_value = {key_token: value_token}
    
    dict_token = DictToken(dict_value, 0, 5)
    
    assert dict_token._child_keys == {"key": key_token}
    assert dict_token._child_tokens == {"key": value_token}

def test_dict_token_get_value():
    key_token = MockToken("key", 0, 1)
    value_token = MockToken("value", 2, 5)
    dict_value = {key_token: value_token}
    
    dict_token = DictToken(dict_value, 0, 5)
    
    assert dict_token._get_value() == {"key": "value"}

def test_dict_token_get_child_token():
    key_token = MockToken("key", 0, 1)
    value_token = MockToken("value", 2, 5)
    dict_value = {key_token: value_token}
    
    dict_token = DictToken(dict_value, 0, 5)
    
    assert dict_token._get_child_token("key") == value_token

def test_dict_token_get_key_token():
    key_token = MockToken("key", 0, 1)
    value_token = MockToken("value", 2, 5)
    dict_value = {key_token: value_token}
    
    dict_token = DictToken(dict_value, 0, 5)
    
    assert dict_token._get_key_token("key") == key_token
