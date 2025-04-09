# file: pymonet/either.py:127-136
# asked: {"lines": [127, 134, 136], "branches": []}
# gained: {"lines": [127], "branches": []}

import pytest
from pymonet.either import Either
from pymonet.maybe import Maybe

class TestLeft:
    def test_to_maybe(self):
        class Left(Either):
            def to_maybe(self):
                from pymonet.maybe import Maybe
                return Maybe.nothing()

        left_instance = Left("error")
        maybe_instance = left_instance.to_maybe()

        assert isinstance(maybe_instance, Maybe)
        assert maybe_instance == Maybe.nothing()
