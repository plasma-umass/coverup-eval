# file: typesystem/tokenize/tokens.py:74-79
# asked: {"lines": [76, 79], "branches": []}
# gained: {"lines": [76, 79], "branches": []}

import pytest
from typesystem.tokenize.tokens import ScalarToken

class MockToken(ScalarToken):
    def __init__(self, value):
        self._value = value
        super().__init__(value, 0, 0)

def test_scalar_token_hash():
    token = MockToken("test_value")
    assert hash(token) == hash("test_value")

def test_scalar_token_get_value():
    token = MockToken("test_value")
    assert token._get_value() == "test_value"
