# file: pymonet/either.py:59-68
# asked: {"lines": [59, 66, 68], "branches": []}
# gained: {"lines": [59, 66, 68], "branches": []}

import pytest
from pymonet.either import Either
from pymonet.monad_try import Try

class TestEither:
    
    def test_to_try_right(self):
        class RightEither(Either):
            def __init__(self, value):
                self.value = value
            
            def is_right(self):
                return True
        
        right_either = RightEither(10)
        result = right_either.to_try()
        
        assert isinstance(result, Try)
        assert result.value == 10
        assert result.is_success is True

    def test_to_try_left(self):
        class LeftEither(Either):
            def __init__(self, value):
                self.value = value
            
            def is_right(self):
                return False
        
        left_either = LeftEither("error")
        result = left_either.to_try()
        
        assert isinstance(result, Try)
        assert result.value == "error"
        assert result.is_success is False
