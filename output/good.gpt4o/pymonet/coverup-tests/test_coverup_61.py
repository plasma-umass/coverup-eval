# file pymonet/either.py:127-136
# lines [127, 134, 136]
# branches []

import pytest
from pymonet.either import Either

def test_left_to_maybe():
    from pymonet.maybe import Maybe

    class Left(Either):
        def __init__(self, value):
            self.value = value

        def to_maybe(self):
            from pymonet.maybe import Maybe
            return Maybe.nothing()

    left_instance = Left(value=None)
    maybe_result = left_instance.to_maybe()

    assert maybe_result == Maybe.nothing()
