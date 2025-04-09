# file: pymonet/validation.py:124-133
# asked: {"lines": [131, 133], "branches": []}
# gained: {"lines": [131, 133], "branches": []}

import pytest
from pymonet.validation import Validation
from pymonet.box import Box

def test_validation_to_box():
    # Create a Validation instance
    validation = Validation("test_value", [])

    # Convert to Box
    box = validation.to_box()

    # Assert the box contains the correct value
    assert isinstance(box, Box)
    assert box.value == "test_value"
