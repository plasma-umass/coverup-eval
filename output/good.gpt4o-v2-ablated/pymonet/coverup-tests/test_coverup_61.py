# file: pymonet/either.py:164-173
# asked: {"lines": [164, 173], "branches": []}
# gained: {"lines": [164], "branches": []}

import pytest
from pymonet.either import Either

class TestRight:
    def test_bind(self):
        class Right(Either):
            def __init__(self, value):
                self.value = value

            def bind(self, mapper):
                return mapper(self.value)

        def mapper_function(x):
            return Right(x + 1)

        right_instance = Right(5)
        result = right_instance.bind(mapper_function)

        assert isinstance(result, Right)
        assert result.value == 6
