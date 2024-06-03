# file typesystem/tokenize/tokens.py:82-98
# lines [82, 83, 84, 85, 86, 88, 89, 90, 91, 94, 95, 97, 98]
# branches []

import pytest
from typesystem.tokenize.tokens import DictToken, Token

class MockToken(Token):
    def __init__(self, value):
        self._value = value

    def _get_value(self):
        return self._value

    def __hash__(self):
        return hash(self._value)

    def __eq__(self, other):
        return isinstance(other, MockToken) and self._value == other._value

@pytest.fixture
def dict_token():
    key1 = MockToken("key1")
    key2 = MockToken("key2")
    value1 = MockToken("value1")
    value2 = MockToken("value2")
    value = {key1: value1, key2: value2}
    return DictToken(value, start_index=0, end_index=0)

def test_dict_token_get_value(dict_token):
    expected_value = {"key1": "value1", "key2": "value2"}
    assert dict_token._get_value() == expected_value

def test_dict_token_get_child_token(dict_token):
    assert dict_token._get_child_token("key1")._get_value() == "value1"
    assert dict_token._get_child_token("key2")._get_value() == "value2"

def test_dict_token_get_key_token(dict_token):
    assert dict_token._get_key_token("key1")._get_value() == "key1"
    assert dict_token._get_key_token("key2")._get_value() == "key2"
