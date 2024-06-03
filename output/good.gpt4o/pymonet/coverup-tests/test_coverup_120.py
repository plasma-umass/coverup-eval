# file pymonet/either.py:81-82
# lines [82]
# branches []

import pytest
from pymonet.either import Either

def test_is_right_not_implemented():
    either_instance = Either(value=None)
    assert either_instance.is_right() is None
