# file: pymonet/either.py:138-147
# asked: {"lines": [138, 145, 147], "branches": []}
# gained: {"lines": [138, 145, 147], "branches": []}

import pytest
from pymonet.either import Left
from pymonet.validation import Validation

class TestLeft:
    def test_to_validation(self):
        # Create an instance of Left with a sample value
        left_instance = Left("error_value")
        
        # Call the to_validation method
        validation_result = left_instance.to_validation()
        
        # Assert that the result is a failed Validation with the correct error value
        assert isinstance(validation_result, Validation)
        assert validation_result.value is None
        assert validation_result.errors == ["error_value"]
