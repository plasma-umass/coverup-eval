# file: typesystem/base.py:187-188
# asked: {"lines": [188], "branches": []}
# gained: {"lines": [188], "branches": []}

import pytest
from typesystem.base import BaseError, ValidationError

def test_base_error_eq_with_validation_error():
    error1 = ValidationError(text="Error 1")
    error2 = ValidationError(text="Error 1")
    assert error1 == error2

def test_base_error_eq_with_non_validation_error():
    error1 = ValidationError(text="Error 1")
    error2 = BaseError(text="Error 1")
    assert error1 != error2
