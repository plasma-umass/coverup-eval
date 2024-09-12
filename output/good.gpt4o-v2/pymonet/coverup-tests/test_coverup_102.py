# file: pymonet/either.py:59-68
# asked: {"lines": [59, 66, 68], "branches": []}
# gained: {"lines": [59, 66, 68], "branches": []}

import pytest
from pymonet.either import Either
from pymonet.monad_try import Try

class Right(Either):
    def is_right(self):
        return True

class Left(Either):
    def is_right(self):
        return False

class TestEitherToTry:
    
    def test_either_right_to_try(self):
        either = Right("success")
        result = either.to_try()
        assert isinstance(result, Try)
        assert result.is_success
        assert result.value == "success"

    def test_either_left_to_try(self):
        either = Left("error")
        result = either.to_try()
        assert isinstance(result, Try)
        assert not result.is_success
        assert result.value == "error"
