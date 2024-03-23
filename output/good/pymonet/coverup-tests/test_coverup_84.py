# file pymonet/box.py:103-112
# lines [103, 110, 112]
# branches []

import pytest
from pymonet.box import Box
from pymonet.validation import Validation

def test_box_to_validation():
    # Create a Box instance with some value
    box = Box(42)

    # Convert the Box to a Validation
    validation = box.to_validation()

    # Assert that the result is a Validation instance
    assert isinstance(validation, Validation)

    # Assert that the Validation is successful and contains the correct value
    assert validation.is_success() is True
    assert validation.value == 42

    # Clean up is not necessary here as no external state is modified
