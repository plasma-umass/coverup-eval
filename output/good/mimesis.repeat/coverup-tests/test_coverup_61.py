# file mimesis/random.py:48-54
# lines [48, 49, 54]
# branches []

import os
import pytest
from mimesis.random import Random

def test_urandom():
    # Test the urandom method with a specific length
    length = 10
    random_bytes = Random.urandom(length)
    assert isinstance(random_bytes, bytes), "urandom should return a bytes object"
    assert len(random_bytes) == length, "urandom should return the specified number of bytes"
