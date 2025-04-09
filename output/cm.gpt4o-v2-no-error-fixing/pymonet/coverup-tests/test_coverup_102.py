# file: pymonet/validation.py:135-144
# asked: {"lines": [142, 144], "branches": []}
# gained: {"lines": [142, 144], "branches": []}

import pytest
from pymonet.validation import Validation
from pymonet.lazy import Lazy

def test_validation_to_lazy():
    # Create a Validation instance
    validation_instance = Validation(value="test_value", errors=[])

    # Convert to Lazy
    lazy_instance = validation_instance.to_lazy()

    # Assert that the returned instance is of type Lazy
    assert isinstance(lazy_instance, Lazy)

    # Assert that the Lazy instance, when evaluated, returns the correct value
    assert lazy_instance.constructor_fn() == "test_value"
