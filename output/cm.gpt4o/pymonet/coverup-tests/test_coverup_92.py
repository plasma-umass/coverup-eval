# file pymonet/either.py:150-152
# lines [150, 151]
# branches []

import pytest
from pymonet.either import Either

def test_right_class():
    class Right(Either):
        """Not successfully Either"""
        def __init__(self, value):
            super().__init__(value)
    
    right_instance = Right("test_value")
    
    assert isinstance(right_instance, Either)
    assert isinstance(right_instance, Right)
    assert right_instance.value == "test_value"
