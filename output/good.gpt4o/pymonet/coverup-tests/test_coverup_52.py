# file pymonet/either.py:189-198
# lines [189, 196, 198]
# branches []

import pytest
from pymonet.either import Either

class TestRight:
    def test_to_maybe(self, mocker):
        from pymonet.maybe import Maybe

        class Right(Either):
            def __init__(self, value):
                self.value = value

            def to_maybe(self):
                from pymonet.maybe import Maybe
                return Maybe.just(self.value)

        value = 42
        right_instance = Right(value)
        maybe_instance = right_instance.to_maybe()

        assert isinstance(maybe_instance, Maybe)
        assert maybe_instance.get_or_else(None) == value
