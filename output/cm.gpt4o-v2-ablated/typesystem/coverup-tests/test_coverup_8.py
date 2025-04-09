# file: typesystem/fields.py:206-236
# asked: {"lines": [206, 209, 210, 211, 212, 213, 214, 217, 219, 220, 221, 222, 224, 225, 227, 228, 231, 232, 233, 234, 235, 236], "branches": []}
# gained: {"lines": [206, 209, 210, 211, 212, 213, 214, 217, 219, 220, 221, 222, 224, 225, 227, 228, 231, 232, 233, 234, 235, 236], "branches": []}

import pytest
import decimal
from typesystem.fields import Number

def test_number_initialization():
    # Test with all None values
    num = Number()
    assert num.minimum is None
    assert num.maximum is None
    assert num.exclusive_minimum is None
    assert num.exclusive_maximum is None
    assert num.multiple_of is None
    assert num.precision is None

    # Test with valid int values
    num = Number(minimum=1, maximum=10, exclusive_minimum=0, exclusive_maximum=11, multiple_of=2)
    assert num.minimum == 1
    assert num.maximum == 10
    assert num.exclusive_minimum == 0
    assert num.exclusive_maximum == 11
    assert num.multiple_of == 2

    # Test with valid float values
    num = Number(minimum=1.1, maximum=10.1, exclusive_minimum=0.1, exclusive_maximum=11.1, multiple_of=2.1)
    assert num.minimum == 1.1
    assert num.maximum == 10.1
    assert num.exclusive_minimum == 0.1
    assert num.exclusive_maximum == 11.1
    assert num.multiple_of == 2.1

    # Test with valid decimal values
    num = Number(
        minimum=decimal.Decimal('1.1'),
        maximum=decimal.Decimal('10.1'),
        exclusive_minimum=decimal.Decimal('0.1'),
        exclusive_maximum=decimal.Decimal('11.1'),
        multiple_of=decimal.Decimal('2.1')
    )
    assert num.minimum == decimal.Decimal('1.1')
    assert num.maximum == decimal.Decimal('10.1')
    assert num.exclusive_minimum == decimal.Decimal('0.1')
    assert num.exclusive_maximum == decimal.Decimal('11.1')
    assert num.multiple_of == decimal.Decimal('2.1')

    # Test with precision
    num = Number(precision='0.01')
    assert num.precision == '0.01'

def test_number_invalid_initialization():
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
