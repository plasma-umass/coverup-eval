# file: typesystem/base.py:219-254
# asked: {"lines": [248, 251, 252, 253, 254], "branches": [[252, 253], [252, 254]]}
# gained: {"lines": [248, 251, 252, 253, 254], "branches": [[252, 253], [252, 254]]}

import pytest
from typesystem.base import ValidationResult, ValidationError

def test_validation_result_bool():
    # Test when there is no error
    result = ValidationResult(value="valid data")
    assert bool(result) is True

    # Test when there is an error
    error = ValidationError(text="Invalid data")
    result = ValidationResult(error=error)
    assert bool(result) is False

def test_validation_result_repr():
    # Test __repr__ when there is an error
    error = ValidationError(text="Invalid data")
    result = ValidationResult(error=error)
    class_name = result.__class__.__name__
    assert repr(result) == f"{class_name}(error={error!r})"

    # Test __repr__ when there is a value
    result = ValidationResult(value="valid data")
    class_name = result.__class__.__name__
    assert repr(result) == f"{class_name}(value='valid data')"
