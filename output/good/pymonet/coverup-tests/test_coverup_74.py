# file pymonet/either.py:120-125
# lines [120, 125]
# branches []

import pytest
from pymonet.either import Left

@pytest.fixture
def left_value():
    return Left('error')

def test_left_is_right(left_value):
    assert left_value.is_right() is False
