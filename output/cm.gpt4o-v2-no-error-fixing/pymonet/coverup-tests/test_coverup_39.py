# file: pymonet/validation.py:8-14
# asked: {"lines": [8, 12, 13, 14], "branches": []}
# gained: {"lines": [8, 12, 13, 14], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_eq():
    val1 = Validation(value=10, errors=[])
    val2 = Validation(value=10, errors=[])
    val3 = Validation(value=20, errors=['error'])
    val4 = "Not a Validation object"

    # Test equality with same values and errors
    assert val1 == val2

    # Test inequality with different values and errors
    assert val1 != val3

    # Test inequality with different type
    assert val1 != val4
