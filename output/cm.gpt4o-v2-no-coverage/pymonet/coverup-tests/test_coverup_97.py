# file: pymonet/validation.py:54-61
# asked: {"lines": [54, 61], "branches": []}
# gained: {"lines": [54, 61], "branches": []}

import pytest
from pymonet.validation import Validation

def test_is_fail_with_errors():
    validation = Validation(value=None, errors=["error1"])
    assert validation.is_fail() is True

def test_is_fail_without_errors():
    validation = Validation(value=None, errors=[])
    assert validation.is_fail() is False
