# file: pymonet/either.py:189-198
# asked: {"lines": [189, 196, 198], "branches": []}
# gained: {"lines": [189], "branches": []}

import pytest
from pymonet.either import Either

class TestRight:
    def test_to_maybe(self, monkeypatch):
        from pymonet.maybe import Maybe

        class MockMaybe:
            @staticmethod
            def just(value):
                return f"MockMaybe.just({value})"

        monkeypatch.setattr(Maybe, 'just', MockMaybe.just)

        class Right(Either):
            def __init__(self, value):
                self.value = value

            def to_maybe(self):
                from pymonet.maybe import Maybe
                return Maybe.just(self.value)

        right_instance = Right(42)
        result = right_instance.to_maybe()
        assert result == "MockMaybe.just(42)"
