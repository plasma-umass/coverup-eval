# file: pymonet/either.py:164-173
# asked: {"lines": [173], "branches": []}
# gained: {"lines": [173], "branches": []}

import pytest
from pymonet.either import Right

class TestRight:
    def test_bind_executes_mapper(self):
        right_instance = Right(5)
        
        def mapper(x):
            return Right(x + 1)
        
        result = right_instance.bind(mapper)
        assert result == Right(6)

    def test_bind_with_different_mapper(self):
        right_instance = Right(10)
        
        def mapper(x):
            return Right(x * 2)
        
        result = right_instance.bind(mapper)
        assert result == Right(20)
