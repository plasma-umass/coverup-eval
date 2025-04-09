# file: pymonet/either.py:164-173
# asked: {"lines": [164, 173], "branches": []}
# gained: {"lines": [164], "branches": []}

import pytest
from pymonet.either import Either

class TestRightBind:
    def test_right_bind_executes_mapper(self):
        class Right(Either):
            def __init__(self, value):
                self.value = value

            def bind(self, mapper):
                return mapper(self.value)

        def mapper_function(value):
            return value * 2

        right_instance = Right(10)
        result = right_instance.bind(mapper_function)
        assert result == 20

    def test_right_bind_with_different_mapper(self):
        class Right(Either):
            def __init__(self, value):
                self.value = value

            def bind(self, mapper):
                return mapper(self.value)

        def mapper_function(value):
            return f"Value is {value}"

        right_instance = Right(10)
        result = right_instance.bind(mapper_function)
        assert result == "Value is 10"
