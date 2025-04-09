# file pymonet/validation.py:74-83
# lines [74, 83]
# branches []

import pytest
from pymonet.validation import Validation

def test_validation_bind():
    class MockValidation(Validation):
        def __init__(self, value):
            self.value = value

    def folder_function(value):
        return MockValidation(value * 2)

    validation_instance = MockValidation(10)
    result = validation_instance.bind(folder_function)

    assert isinstance(result, Validation)
    assert result.value == 20

# Cleanup is not necessary in this case as we are not modifying any global state,
# and the MockValidation class is contained within the test function.
