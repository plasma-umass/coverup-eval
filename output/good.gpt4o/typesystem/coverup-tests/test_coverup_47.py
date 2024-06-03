# file typesystem/fields.py:309-313
# lines [309, 310, 312, 313]
# branches []

import pytest
import decimal
import typing
from typesystem.fields import Number

class Decimal(Number):
    numeric_type = decimal.Decimal

    def serialize(self, obj: typing.Any) -> typing.Any:
        return None if obj is None else float(obj)

def test_decimal_serialize():
    decimal_field = Decimal()

    # Test serialization of None
    assert decimal_field.serialize(None) is None

    # Test serialization of a decimal value
    dec_value = decimal.Decimal('10.5')
    assert decimal_field.serialize(dec_value) == 10.5

    # Test serialization of a zero decimal value
    zero_value = decimal.Decimal('0.0')
    assert decimal_field.serialize(zero_value) == 0.0

    # Test serialization of a negative decimal value
    neg_value = decimal.Decimal('-5.5')
    assert decimal_field.serialize(neg_value) == -5.5
