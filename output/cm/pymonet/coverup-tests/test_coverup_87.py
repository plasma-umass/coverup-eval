# file pymonet/validation.py:63-72
# lines [63, 72]
# branches []

import pytest
from pymonet.validation import Validation

def test_validation_map():
    initial_value = 10
    expected_mapped_value = 20
    mapper_function = lambda x: x * 2
    validation_instance = Validation(initial_value, [])

    # Apply the map function
    mapped_validation = validation_instance.map(mapper_function)

    # Check if the value is mapped correctly
    assert mapped_validation.value == expected_mapped_value
    # Check if the errors remain unchanged
    assert mapped_validation.errors == validation_instance.errors
