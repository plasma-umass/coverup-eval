# file pymonet/validation.py:85-96
# lines [96]
# branches []

import pytest
from pymonet.validation import Validation

class TestValidation:
    def test_ap_executes_line_96(self):
        # Mock function to be passed to ap
        def mock_fn(value):
            return Validation(value, ["new error"])

        # Create a Validation instance with initial value and errors
        validation_instance = Validation("initial value", ["initial error"])

        # Call the ap method with the mock function
        new_validation = validation_instance.ap(mock_fn)

        # Assertions to verify the postconditions
        assert new_validation.value == "initial value"
        assert new_validation.errors == ["initial error", "new error"]
