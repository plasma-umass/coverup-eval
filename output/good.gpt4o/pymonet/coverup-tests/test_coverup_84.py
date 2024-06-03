# file pymonet/either.py:97-104
# lines [97, 104]
# branches []

import pytest
from pymonet.either import Either

def test_left_bind():
    class Left(Either):
        def __init__(self, value):
            self.value = value

        def bind(self, _):
            return self

    left_instance = Left("error")
    result = left_instance.bind(lambda x: x + 1)
    
    assert isinstance(result, Left)
    assert result.value == "error"
