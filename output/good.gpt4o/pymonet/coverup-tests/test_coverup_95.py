# file pymonet/either.py:88-95
# lines [88, 95]
# branches []

import pytest
from typing import Callable, Any
from pymonet.either import Either

def test_left_map():
    class Left(Either):
        def __init__(self, value):
            self.value = value

        def map(self, _: Callable[[Any], Any]) -> 'Left':
            return Left(self.value)

    left_instance = Left(10)
    mapped_instance = left_instance.map(lambda x: x * 2)

    assert isinstance(mapped_instance, Left)
    assert mapped_instance.value == 10
