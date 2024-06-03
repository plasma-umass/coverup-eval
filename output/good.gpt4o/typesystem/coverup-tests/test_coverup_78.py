# file typesystem/fields.py:309-313
# lines [313]
# branches []

import pytest
from typesystem.fields import Decimal
import decimal

def test_decimal_serialize():
    decimal_field = Decimal()

    # Test when obj is None
    result = decimal_field.serialize(None)
    assert result is None, "Expected None when input is None"

    # Test when obj is a decimal.Decimal
    obj = decimal.Decimal('10.5')
    result = decimal_field.serialize(obj)
    assert result == float(obj), f"Expected {float(obj)} when input is {obj}"

    # Test when obj is a float
    obj = 10.5
    result = decimal_field.serialize(obj)
    assert result == float(obj), f"Expected {float(obj)} when input is {obj}"

    # Test when obj is an integer
    obj = 10
    result = decimal_field.serialize(obj)
    assert result == float(obj), f"Expected {float(obj)} when input is {obj}"
