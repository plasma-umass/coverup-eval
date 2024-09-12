# file: typesystem/tokenize/tokens.py:66-71
# asked: {"lines": [66, 67, 68, 69, 70], "branches": []}
# gained: {"lines": [66, 67, 68, 69, 70], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self, value, start_index, end_index):
        self._value = value
        self._start_index = start_index
        self._end_index = end_index

    def _get_value(self):
        return self._value

def test_token_equality():
    token1 = MockToken(value="test", start_index=0, end_index=4)
    token2 = MockToken(value="test", start_index=0, end_index=4)
    token3 = MockToken(value="test", start_index=0, end_index=5)
    token4 = MockToken(value="different", start_index=0, end_index=4)
    token5 = "not_a_token"

    assert token1 == token2  # Should be True
    assert token1 != token3  # Should be False due to different end_index
    assert token1 != token4  # Should be False due to different value
    assert token1 != token5  # Should be False due to different type
