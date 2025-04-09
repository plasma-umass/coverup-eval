# file: dataclasses_json/core.py:211-231
# asked: {"lines": [211, 212, 216, 217, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 230, 231], "branches": [[212, 216], [212, 221], [216, 217], [216, 219], [221, 222], [221, 225], [225, 226], [225, 230]]}
# gained: {"lines": [211, 212, 216, 217, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 230, 231], "branches": [[212, 216], [212, 221], [216, 217], [216, 219], [221, 222], [221, 225], [225, 226], [225, 230]]}

import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
from dataclasses_json.utils import _issubclass_safe
from dataclasses_json.core import _support_extended_types

def test_support_extended_types_datetime():
    # Test with datetime type and datetime value
    dt = datetime.now()
    assert _support_extended_types(datetime, dt) == dt

    # Test with datetime type and timestamp value
    timestamp = dt.timestamp()
    result = _support_extended_types(datetime, timestamp)
    assert isinstance(result, datetime)
    assert result.timestamp() == pytest.approx(timestamp, rel=1e-6)

def test_support_extended_types_decimal():
    # Test with Decimal type and Decimal value
    dec = Decimal('10.5')
    assert _support_extended_types(Decimal, dec) == dec

    # Test with Decimal type and float value
    float_value = 10.5
    result = _support_extended_types(Decimal, float_value)
    assert isinstance(result, Decimal)
    assert result == Decimal(float_value)

def test_support_extended_types_uuid():
    # Test with UUID type and UUID value
    uuid_val = UUID('12345678123456781234567812345678')
    assert _support_extended_types(UUID, uuid_val) == uuid_val

    # Test with UUID type and string value
    uuid_str = '12345678123456781234567812345678'
    result = _support_extended_types(UUID, uuid_str)
    assert isinstance(result, UUID)
    assert result == UUID(uuid_str)

def test_support_extended_types_other():
    # Test with other types
    assert _support_extended_types(int, 10) == 10
    assert _support_extended_types(str, 'test') == 'test'
