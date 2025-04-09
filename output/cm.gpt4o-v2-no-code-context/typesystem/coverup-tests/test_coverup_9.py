# file: typesystem/fields.py:206-236
# asked: {"lines": [206, 209, 210, 211, 212, 213, 214, 217, 219, 220, 221, 222, 224, 225, 227, 228, 231, 232, 233, 234, 235, 236], "branches": []}
# gained: {"lines": [206, 209, 210, 211, 212, 213, 214, 217, 219, 220, 221, 222, 224, 225, 227, 228, 231, 232, 233, 234, 235, 236], "branches": []}

import pytest
import decimal
from typesystem.fields import Number

def test_number_field_initialization():
    # Test with all parameters set to None
    field = Number()
    assert field.minimum is None
    assert field.maximum is None
    assert field.exclusive_minimum is None
    assert field.exclusive_maximum is None
    assert field.multiple_of is None
    assert field.precision is None

    # Test with valid integer values
    field = Number(minimum=1, maximum=10, exclusive_minimum=2, exclusive_maximum=9, multiple_of=1)
    assert field.minimum == 1
    assert field.maximum == 10
    assert field.exclusive_minimum == 2
    assert field.exclusive_maximum == 9
    assert field.multiple_of == 1

    # Test with valid float values
    field = Number(minimum=1.1, maximum=10.1, exclusive_minimum=2.1, exclusive_maximum=9.1, multiple_of=1.1)
    assert field.minimum == 1.1
    assert field.maximum == 10.1
    assert field.exclusive_minimum == 2.1
    assert field.exclusive_maximum == 9.1
    assert field.multiple_of == 1.1

    # Test with valid decimal values
    field = Number(
        minimum=decimal.Decimal('1.1'),
        maximum=decimal.Decimal('10.1'),
        exclusive_minimum=decimal.Decimal('2.1'),
        exclusive_maximum=decimal.Decimal('9.1'),
        multiple_of=decimal.Decimal('1.1')
    )
    assert field.minimum == decimal.Decimal('1.1')
    assert field.maximum == decimal.Decimal('10.1')
    assert field.exclusive_minimum == decimal.Decimal('2.1')
    assert field.exclusive_maximum == decimal.Decimal('9.1')
    assert field.multiple_of == decimal.Decimal('1.1')

    # Test with precision
    field = Number(precision='0.01')
    assert field.precision == '0.01'

def test_number_field_invalid_initialization():
    # Test with invalid minimum type
    with pytest.raises(AssertionError):
        Number(minimum='invalid')

    # Test with invalid maximum type
    with pytest.raises(AssertionError):
        Number(maximum='invalid')

    # Test with invalid exclusive_minimum type
    with pytest.raises(AssertionError):
        Number(exclusive_minimum='invalid')

    # Test with invalid exclusive_maximum type
    with pytest.raises(AssertionError):
        Number(exclusive_maximum='invalid')

    # Test with invalid multiple_of type
    with pytest.raises(AssertionError):
        Number(multiple_of='invalid')
