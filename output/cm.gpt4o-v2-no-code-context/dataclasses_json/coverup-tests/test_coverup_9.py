# file: dataclasses_json/core.py:211-231
# asked: {"lines": [211, 212, 216, 217, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 230, 231], "branches": [[212, 216], [212, 221], [216, 217], [216, 219], [221, 222], [221, 225], [225, 226], [225, 230]]}
# gained: {"lines": [211, 212, 216, 217, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 230, 231], "branches": [[212, 216], [212, 221], [216, 217], [216, 219], [221, 222], [221, 225], [225, 226], [225, 230]]}

import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
from dataclasses_json.core import _support_extended_types

def _issubclass_safe(cls, classinfo):
    try:
        return issubclass(cls, classinfo)
    except TypeError:
        return False

def test_support_extended_types_datetime_instance():
    dt = datetime.now()
    result = _support_extended_types(datetime, dt)
    assert result == dt

def test_support_extended_types_datetime_timestamp():
    timestamp = 1638316800  # Corresponds to 2021-12-01 00:00:00 UTC
    result = _support_extended_types(datetime, timestamp)
    assert isinstance(result, datetime)
    assert result.timestamp() == timestamp

def test_support_extended_types_decimal_instance():
    dec = Decimal('10.5')
    result = _support_extended_types(Decimal, dec)
    assert result == dec

def test_support_extended_types_decimal_value():
    value = '10.5'
    result = _support_extended_types(Decimal, value)
    assert isinstance(result, Decimal)
    assert result == Decimal(value)

def test_support_extended_types_uuid_instance():
    uuid_val = UUID('12345678123456781234567812345678')
    result = _support_extended_types(UUID, uuid_val)
    assert result == uuid_val

def test_support_extended_types_uuid_value():
    value = '12345678123456781234567812345678'
    result = _support_extended_types(UUID, value)
    assert isinstance(result, UUID)
    assert result == UUID(value)

def test_support_extended_types_fallback():
    value = 'some_string'
    result = _support_extended_types(str, value)
    assert result == value
