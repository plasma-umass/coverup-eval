# file: pymonet/either.py:37-46
# asked: {"lines": [37, 46], "branches": []}
# gained: {"lines": [37, 46], "branches": []}

import pytest
from pymonet.either import Either

class TestEither:
    def test_ap(self):
        class MockApplicative(Either):
            def map(self, value):
                return f"mapped {value}"

        # Create instances of Either and MockApplicative
        either_instance = Either('value')
        applicative_instance = MockApplicative(lambda x: x * 2)

        # Call the ap method
        result = either_instance.ap(applicative_instance)

        # Assertions
        assert result == "mapped value"
