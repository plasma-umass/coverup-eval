# file: pymonet/validation.py:8-14
# asked: {"lines": [8, 12, 13, 14], "branches": []}
# gained: {"lines": [8, 12, 13, 14], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_eq():
    # Test equality with same values and errors
    v1 = Validation(value=10, errors=[])
    v2 = Validation(value=10, errors=[])
    assert v1 == v2

    # Test inequality with different values
    v3 = Validation(value=20, errors=[])
    assert v1 != v3

    # Test inequality with different errors
    v4 = Validation(value=10, errors=['error'])
    assert v1 != v4

    # Test inequality with different type
    assert v1 != 10
