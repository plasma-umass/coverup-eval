# file: typesystem/fields.py:309-313
# asked: {"lines": [313], "branches": []}
# gained: {"lines": [313], "branches": []}

import pytest
import decimal
from typesystem.fields import Decimal

@pytest.fixture
def decimal_field():
    return Decimal()

def test_decimal_serialize_none(decimal_field):
    assert decimal_field.serialize(None) is None

def test_decimal_serialize_decimal(decimal_field):
    value = decimal.Decimal('10.5')
    assert decimal_field.serialize(value) == 10.5

def test_decimal_serialize_int(decimal_field):
    value = 5
    assert decimal_field.serialize(value) == 5.0

def test_decimal_serialize_float(decimal_field):
    value = 3.14
    assert decimal_field.serialize(value) == 3.14
