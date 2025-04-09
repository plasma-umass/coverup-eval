# file: pymonet/validation.py:45-52
# asked: {"lines": [45, 52], "branches": []}
# gained: {"lines": [45, 52], "branches": []}

import pytest
from pymonet.validation import Validation

def test_is_success_with_no_errors():
    validation = Validation(value="some_value", errors=[])
    assert validation.is_success() is True

def test_is_success_with_errors():
    validation = Validation(value="some_value", errors=["error1", "error2"])
    assert validation.is_success() is False
