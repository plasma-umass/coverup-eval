# file pymonet/either.py:88-95
# lines [95]
# branches []

import pytest
from pymonet.either import Left

def test_left_map():
    left_instance = Left(10)
    mapped_instance = left_instance.map(lambda x: x * 2)
    
    assert isinstance(mapped_instance, Left)
    assert mapped_instance.value == 10

    # Ensure line 95 is executed
    assert mapped_instance is not left_instance
