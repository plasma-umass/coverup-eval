# file: typesystem/fields.py:206-236
# asked: {"lines": [206, 209, 210, 211, 212, 213, 214, 217, 219, 220, 221, 222, 224, 225, 227, 228, 231, 232, 233, 234, 235, 236], "branches": []}
# gained: {"lines": [206, 209, 210, 211, 212, 213, 214, 217, 219, 220, 221, 222, 224, 225, 227, 228, 231, 232, 233, 234, 235, 236], "branches": []}

import pytest
import decimal
from typesystem.fields import Number

def test_number_init_with_valid_values():
    num = Number(minimum=1, maximum=10, exclusive_minimum=0, exclusive_maximum=11, precision="0.01", multiple_of=1)
    assert num.minimum == 1
    assert num.maximum == 10
    assert num.exclusive_minimum == 0
    assert num.exclusive_maximum == 11
    assert num.precision == "0.01"
    assert num.multiple_of == 1

def test_number_init_with_none_values():
    num = Number()
    assert num.minimum is None
    assert num.maximum is None
    assert num.exclusive_minimum is None
    assert num.exclusive_maximum is None
    assert num.precision is None
    assert num.multiple_of is None

def test_number_init_with_invalid_minimum():
    with pytest.raises(AssertionError):
        Number(minimum="invalid")

def test_number_init_with_invalid_maximum():
    with pytest.raises(AssertionError):
        Number(maximum="invalid")

def test_number_init_with_invalid_exclusive_minimum():
    with pytest.raises(AssertionError):
        Number(exclusive_minimum="invalid")

def test_number_init_with_invalid_exclusive_maximum():
    with pytest.raises(AssertionError):
        Number(exclusive_maximum="invalid")

def test_number_init_with_invalid_multiple_of():
    with pytest.raises(AssertionError):
        Number(multiple_of="invalid")
