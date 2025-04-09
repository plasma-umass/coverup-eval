# file: pymonet/either.py:189-198
# asked: {"lines": [189, 196, 198], "branches": []}
# gained: {"lines": [189, 196, 198], "branches": []}

import pytest
from pymonet.either import Either, Right
from pymonet.maybe import Maybe

class TestRight:
    def test_to_maybe(self):
        value = 42
        right_instance = Right(value)
        maybe_instance = right_instance.to_maybe()
        
        assert isinstance(maybe_instance, Maybe)
        assert maybe_instance == Maybe.just(value)
