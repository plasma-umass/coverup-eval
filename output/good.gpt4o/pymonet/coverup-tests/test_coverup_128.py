# file pymonet/either.py:59-68
# lines [66, 68]
# branches []

import pytest
from pymonet.either import Either
from pymonet.monad_try import Try

def test_either_to_try(mocker):
    # Mock the is_right method to control the flow
    mocker.patch.object(Either, 'is_right', return_value=True)
    
    # Create an instance of Either with a value
    either_instance = Either("test_value")
    
    # Call the to_try method
    result = either_instance.to_try()
    
    # Assert that the result is an instance of Try
    assert isinstance(result, Try)
    
    # Assert that the value is correctly passed to Try
    assert result.value == "test_value"
    
    # Assert that the Try instance is successful
    assert result.is_success == True
