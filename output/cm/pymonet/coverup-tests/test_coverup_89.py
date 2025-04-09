# file pymonet/maybe.py:101-112
# lines [101, 110, 111, 112]
# branches ['110->111', '110->112']

import pytest
from pymonet.maybe import Maybe

class Nothing(Maybe):
    def __init__(self):
        self.is_nothing = True
        self.value = None

class Just(Maybe):
    def __init__(self, value):
        self.is_nothing = False
        self.value = value

@pytest.fixture
def nothing_maybe():
    return Nothing()

@pytest.fixture
def just_maybe():
    return Just(10)

def test_get_or_else_with_nothing(nothing_maybe):
    default_value = 5
    result = nothing_maybe.get_or_else(default_value)
    assert result == default_value

def test_get_or_else_with_just(just_maybe):
    default_value = 5
    result = just_maybe.get_or_else(default_value)
    assert result == just_maybe.value
