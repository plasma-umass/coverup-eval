# file: pymonet/validation.py:45-52
# asked: {"lines": [45, 52], "branches": []}
# gained: {"lines": [45, 52], "branches": []}

import pytest
from pymonet.validation import Validation

def test_is_success_with_empty_errors():
    validation = Validation(value="some_value", errors=[])
    assert validation.is_success() == True

def test_is_success_with_non_empty_errors():
    validation = Validation(value="some_value", errors=["error1"])
    assert validation.is_success() == False
