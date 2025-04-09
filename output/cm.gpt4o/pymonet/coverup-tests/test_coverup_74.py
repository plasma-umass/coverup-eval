# file pymonet/either.py:14-15
# lines [14, 15]
# branches []

import pytest
from pymonet.either import Either

def test_either_initialization():
    # Test initialization with a value
    value = 42
    either_instance = Either(value)
    assert either_instance.value == value

    # Test initialization with a different type of value
    value = "test"
    either_instance = Either(value)
    assert either_instance.value == value

    # Test initialization with None
    value = None
    either_instance = Either(value)
    assert either_instance.value is None
