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

def test_token_equality_same(token_a, token_b):
    assert token_a == token_b

def test_token_equality_different_value(token_a, token_c):
    assert token_a != token_c

def test_token_equality_different_start_index(token_a, token_d):
    assert token_a != token_d

def test_token_equality_different_end_index(token_a, token_e):
    assert token_a != token_e

def test_token_equality_different_type(token_a):
    assert token_a != "not_a_token"
