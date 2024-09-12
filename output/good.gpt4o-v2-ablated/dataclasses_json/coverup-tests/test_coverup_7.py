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

@pytest.mark.parametrize("field_type, field_value, expected", [
    (datetime, datetime(2020, 1, 1, tzinfo=timezone.utc), datetime(2020, 1, 1, tzinfo=timezone.utc)),
    (datetime, 1609459200, datetime(2021, 1, 1, tzinfo=timezone.utc)),  # 1609459200 is 2021-01-01 00:00:00 UTC
    (Decimal, Decimal('10.5'), Decimal('10.5')),
    (Decimal, '10.5', Decimal('10.5')),
    (UUID, UUID('12345678123456781234567812345678'), UUID('12345678123456781234567812345678')),
    (UUID, '12345678-1234-5678-1234-567812345678', UUID('12345678-1234-5678-1234-567812345678')),
    (str, 'test', 'test'),
])
def test_support_extended_types(field_type, field_value, expected, monkeypatch):
    def mock_issubclass_safe(cls, classinfo):
        return _issubclass_safe(cls, classinfo)
    
    monkeypatch.setattr('dataclasses_json.core._issubclass_safe', mock_issubclass_safe)
    
    result = _support_extended_types(field_type, field_value)
    assert result == expected
