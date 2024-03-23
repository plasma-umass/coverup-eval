# file typesystem/fields.py:206-236
# lines [206, 209, 210, 211, 212, 213, 214, 217, 219, 220, 221, 222, 224, 225, 227, 228, 231, 232, 233, 234, 235, 236]
# branches []

import decimal
import pytest
from typesystem.fields import Number

def test_number_field_initialization():
    # Test with all parameters set to None
    number_field = Number()
    assert number_field.minimum is None
    assert number_field.maximum is None
    assert number_field.exclusive_minimum is None
    assert number_field.exclusive_maximum is None
    assert number_field.multiple_of is None
    assert number_field.precision is None

    # Test with all parameters set to valid values
    min_val = 0
    max_val = 10
    excl_min_val = 1
    excl_max_val = 9
    multiple_of_val = 2
    precision_val = '0.01'
    number_field = Number(
        minimum=min_val,
        maximum=max_val,
        exclusive_minimum=excl_min_val,
        exclusive_maximum=excl_max_val,
        multiple_of=multiple_of_val,
        precision=precision_val
    )
    assert number_field.minimum == min_val
    assert number_field.maximum == max_val
    assert number_field.exclusive_minimum == excl_min_val
    assert number_field.exclusive_maximum == excl_max_val
    assert number_field.multiple_of == multiple_of_val
    assert number_field.precision == precision_val

    # Test with invalid type for minimum
    with pytest.raises(AssertionError):
        Number(minimum='invalid')

    # Test with invalid type for maximum
    with pytest.raises(AssertionError):
        Number(maximum='invalid')

    # Test with invalid type for exclusive_minimum
    with pytest.raises(AssertionError):
        Number(exclusive_minimum='invalid')

    # Test with invalid type for exclusive_maximum
    with pytest.raises(AssertionError):
        Number(exclusive_maximum='invalid')

    # Test with invalid type for multiple_of
    with pytest.raises(AssertionError):
        Number(multiple_of='invalid')
