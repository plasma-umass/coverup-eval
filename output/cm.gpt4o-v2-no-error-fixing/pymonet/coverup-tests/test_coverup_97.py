# file: pymonet/validation.py:85-96
# asked: {"lines": [85, 96], "branches": []}
# gained: {"lines": [85, 96], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_ap():
    # Create a Validation instance with initial value and errors
    initial_value = 10
    initial_errors = ["initial error"]
    validation = Validation(initial_value, initial_errors)

    # Define a function that returns a new Validation with additional errors
    def fn(value):
        return Validation(value, ["new error"])

    # Apply the function using the ap method
    new_validation = validation.ap(fn)

    # Assert that the new Validation has the same value
    assert new_validation.value == initial_value

    # Assert that the new Validation has concatenated errors
    assert new_validation.errors == initial_errors + ["new error"]

    # Clean up (not strictly necessary in this case, but good practice)
    del validation
    del new_validation
