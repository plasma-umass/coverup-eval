# file: pymonet/validation.py:135-144
# asked: {"lines": [135, 142, 144], "branches": []}
# gained: {"lines": [135, 142, 144], "branches": []}

import pytest
from pymonet.validation import Validation
from pymonet.lazy import Lazy

def test_validation_to_lazy():
    # Create a Validation instance
    validation = Validation("test_value", [])

    # Convert to Lazy
    lazy_result = validation.to_lazy()

    # Assert that the result is an instance of Lazy
    assert isinstance(lazy_result, Lazy)

    # Assert that the Lazy instance contains the correct value
    assert lazy_result.constructor_fn() == "test_value"
