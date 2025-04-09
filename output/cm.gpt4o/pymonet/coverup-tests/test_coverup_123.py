# file pymonet/either.py:37-46
# lines [46]
# branches []

import pytest
from pymonet.either import Either

class TestEither:
    def test_ap_function_applied(self):
        # Mocking the map method to ensure it gets called
        class MockEither(Either):
            def map(self, func):
                self.func_called = True
                return self

        # Create an instance of Either with a value
        either_instance = Either(lambda x: x + 1)

        # Create a mock applicative instance
        applicative_instance = MockEither(None)
        applicative_instance.func_called = False

        # Call the ap method
        result = either_instance.ap(applicative_instance)

        # Assert that the map method was called
        assert applicative_instance.func_called
        # Assert that the result is the same instance as applicative_instance
        assert result is applicative_instance
