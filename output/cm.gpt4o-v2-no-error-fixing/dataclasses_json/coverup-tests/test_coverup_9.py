# file: dataclasses_json/core.py:211-231
# asked: {"lines": [211, 212, 216, 217, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 230, 231], "branches": [[212, 216], [212, 221], [216, 217], [216, 219], [221, 222], [221, 225], [225, 226], [225, 230]]}
# gained: {"lines": [211, 212, 216, 217, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 230, 231], "branches": [[212, 216], [212, 221], [216, 217], [216, 219], [221, 222], [221, 225], [225, 226], [225, 230]]}

import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
from dataclasses_json.core import _support_extended_types

def test_support_extended_types_datetime():
    dt = datetime(2023, 1, 1, tzinfo=timezone.utc)
    assert _support_extended_types(datetime, dt) == dt

    timestamp = 1672531200  # Corresponds to 2023-01-01 00:00:00 UTC
    result = _support_extended_types(datetime, timestamp)
    assert isinstance(result, datetime)
    assert result.timestamp() == timestamp

def test_support_extended_types_decimal():
    dec = Decimal('10.5')
    assert _support_extended_types(Decimal, dec) == dec

    dec_str = '10.5'
    result = _support_extended_types(Decimal, dec_str)
    assert isinstance(result, Decimal)
    assert result == Decimal(dec_str)

def test_support_extended_types_uuid():
    uuid_val = UUID('12345678123456781234567812345678')
    assert _support_extended_types(UUID, uuid_val) == uuid_val

    uuid_str = '12345678-1234-5678-1234-567812345678'
    result = _support_extended_types(UUID, uuid_str)
    assert isinstance(result, UUID)
    assert result == UUID(uuid_str)

def test_support_extended_types_other():
    value = "test_string"
    assert _support_extended_types(str, value) == value
