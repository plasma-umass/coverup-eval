# file: pymonet/either.py:37-46
# asked: {"lines": [37, 46], "branches": []}
# gained: {"lines": [37, 46], "branches": []}

import pytest
from pymonet.either import Either

class TestEither:
    def test_ap(self):
        # Mocking the map method
        class MockEither(Either):
            def map(self, func):
                return func(5)

        # Creating an instance of Either with a function
        either_instance = Either(lambda x: x * 2)
        applicative = MockEither(None)

        # Applying the function inside Either to the applicative
        result = either_instance.ap(applicative)

        # Asserting the result
        assert result == 10
