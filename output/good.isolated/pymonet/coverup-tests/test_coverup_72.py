# file pymonet/either.py:113-118
# lines [113, 118]
# branches []

import pytest
from pymonet.either import Left

@pytest.fixture
def left_value():
    return Left('error')

def test_left_is_left(left_value):
    assert left_value.is_left() is True
