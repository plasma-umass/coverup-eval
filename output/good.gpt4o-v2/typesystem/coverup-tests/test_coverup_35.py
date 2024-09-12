# file: typesystem/fields.py:309-313
# asked: {"lines": [309, 310, 312, 313], "branches": []}
# gained: {"lines": [309, 310, 312, 313], "branches": []}

import pytest
import decimal
from typesystem.fields import Decimal

def test_decimal_serialize_with_none():
    dec = Decimal()
    result = dec.serialize(None)
    assert result is None

def test_decimal_serialize_with_value():
    dec = Decimal()
    value = decimal.Decimal('10.5')
    result = dec.serialize(value)
    assert result == float(value)
