# file: pymonet/either.py:153-162
# asked: {"lines": [153, 162], "branches": []}
# gained: {"lines": [153], "branches": []}

import pytest
from pymonet.either import Either

class TestRight:
    def test_right_map(self):
        class Right(Either):
            def __init__(self, value):
                self.value = value

            def map(self, mapper):
                return Right(mapper(self.value))

        def mapper_function(x):
            return x + 1

        right_instance = Right(10)
        new_right_instance = right_instance.map(mapper_function)

        assert isinstance(new_right_instance, Right)
        assert new_right_instance.value == 11
