# file mimesis/random.py:48-54
# lines [48, 49, 54]
# branches []

import os
import pytest
from mimesis.random import Random

def test_urandom():
    # Test the urandom method with a specific length
    length = 16
    random_bytes = Random.urandom(length)
    assert isinstance(random_bytes, bytes), "The result must be a bytes object"
    assert len(random_bytes) == length, "The length of the bytes object must be equal to the requested length"

    # Test the urandom method with zero length
    zero_length_bytes = Random.urandom(0)
    assert isinstance(zero_length_bytes, bytes), "The result must be a bytes object"
    assert len(zero_length_bytes) == 0, "The length of the bytes object must be zero when requested length is zero"
