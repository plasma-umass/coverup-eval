# file: pymonet/either.py:59-68
# asked: {"lines": [59, 66, 68], "branches": []}
# gained: {"lines": [59, 66, 68], "branches": []}

import pytest
from pymonet.either import Either
from pymonet.monad_try import Try

class TestEither:
    def test_to_try_right(self, mocker):
        # Mock the is_right method to return True
        mocker.patch.object(Either, 'is_right', return_value=True)
        
        # Create an instance of Either with a value
        either_instance = Either("test_value")
        
        # Call the to_try method
        result = either_instance.to_try()
        
        # Assert the result is a Try instance with the correct value and is_success=True
        assert isinstance(result, Try)
        assert result.value == "test_value"
        assert result.is_success is True

    def test_to_try_left(self, mocker):
        # Mock the is_right method to return False
        mocker.patch.object(Either, 'is_right', return_value=False)
        
        # Create an instance of Either with a value
        either_instance = Either("test_value")
        
        # Call the to_try method
        result = either_instance.to_try()
        
        # Assert the result is a Try instance with the correct value and is_success=False
        assert isinstance(result, Try)
        assert result.value == "test_value"
        assert result.is_success is False
