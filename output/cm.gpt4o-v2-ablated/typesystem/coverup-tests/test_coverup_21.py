# file: typesystem/tokenize/tokens.py:66-71
# asked: {"lines": [67, 68, 69, 70], "branches": []}
# gained: {"lines": [67, 68, 69, 70], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self, value, start_index, end_index):
        self._value = value
        self._start_index = start_index
        self._end_index = end_index

    def _get_value(self):
        return self._value

@pytest.fixture
def token_a():
    return MockToken("value", 0, 5)

@pytest.fixture
def token_b():
    return MockToken("value", 0, 5)

@pytest.fixture
def token_c():
    return MockToken("different_value", 0, 5)

@pytest.fixture
def token_d():
    return MockToken("value", 1, 5)

@pytest.fixture
def token_e():
    return MockToken("value", 0, 6)

def test_token_equality(token_a, token_b, token_c, token_d, token_e):
    assert token_a == token_b  # Same value and indices
    assert token_a != token_c  # Different value
    assert token_a != token_d  # Different start index
    assert token_a != token_e  # Different end index
    assert token_a != "not_a_token"  # Different type
