# file: pymonet/either.py:189-198
# asked: {"lines": [189, 196, 198], "branches": []}
# gained: {"lines": [189], "branches": []}

import pytest
from pymonet.either import Either
from pymonet.maybe import Maybe

class TestRight:
    def test_to_maybe(self):
        class Right(Either):
            def to_maybe(self):
                from pymonet.maybe import Maybe
                return Maybe.just(self.value)
        
        right_instance = Right(42)
        maybe_instance = right_instance.to_maybe()
        
        assert isinstance(maybe_instance, Maybe)
        assert maybe_instance.get_or_else(None) == 42
