# file: typesystem/fields.py:309-313
# asked: {"lines": [309, 310, 312, 313], "branches": []}
# gained: {"lines": [309, 310, 312], "branches": []}

import pytest
import decimal
import typing
from typesystem.fields import Number

class Decimal(Number):
    numeric_type = decimal.Decimal

    def serialize(self, obj: typing.Any) -> typing.Any:
        return None if obj is None else float(obj)

@pytest.fixture
def decimal_field():
    return Decimal()

def test_decimal_serialize_none(decimal_field):
    assert decimal_field.serialize(None) is None

def test_decimal_serialize_value(decimal_field):
    assert decimal_field.serialize(decimal.Decimal('10.5')) == 10.5
