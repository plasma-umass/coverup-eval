# file pymonet/either.py:164-173
# lines [164, 173]
# branches []

import pytest
from pymonet.either import Either

class TestRight:
    def test_bind_executes_mapper(self):
        class Right(Either):
            def __init__(self, value):
                self.value = value

            def bind(self, mapper):
                return mapper(self.value)

        def mapper(x):
            return x * 2

        right_instance = Right(10)
        result = right_instance.bind(mapper)
        assert result == 20

    def test_bind_with_different_mapper(self):
        class Right(Either):
            def __init__(self, value):
                self.value = value

            def bind(self, mapper):
                return mapper(self.value)

        def mapper(x):
            return f"Value is {x}"

        right_instance = Right(10)
        result = right_instance.bind(mapper)
        assert result == "Value is 10"
