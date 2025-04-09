# file: typesystem/tokenize/tokens.py:66-71
# asked: {"lines": [66, 67, 68, 69, 70], "branches": []}
# gained: {"lines": [66, 67, 68, 69, 70], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def _get_value(self):
        return self._value

@pytest.fixture
def token_a():
    return MockToken(value="test", start_index=0, end_index=4)

@pytest.fixture
def token_b():
    return MockToken(value="test", start_index=0, end_index=4)

@pytest.fixture
def token_c():
    return MockToken(value="test", start_index=0, end_index=5)

@pytest.fixture
def token_d():
    return MockToken(value="different", start_index=0, end_index=4)

def test_token_equality(token_a, token_b, token_c, token_d):
    # Test equality with identical tokens
    assert token_a == token_b

    # Test inequality with different end_index
    assert token_a != token_c

    # Test inequality with different value
    assert token_a != token_d

    # Test inequality with different type
    assert token_a != "not_a_token"
