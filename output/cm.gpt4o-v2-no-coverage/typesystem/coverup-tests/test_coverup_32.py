# file: typesystem/fields.py:309-313
# asked: {"lines": [309, 310, 312, 313], "branches": []}
# gained: {"lines": [309, 310, 312, 313], "branches": []}

import decimal
import pytest
from typesystem.fields import Decimal

def test_decimal_serialize_none():
    dec = Decimal()
    assert dec.serialize(None) is None

def test_decimal_serialize_value():
    dec = Decimal()
    assert dec.serialize(decimal.Decimal('10.5')) == 10.5

def test_decimal_numeric_type():
    dec = Decimal()
    assert dec.numeric_type == decimal.Decimal
