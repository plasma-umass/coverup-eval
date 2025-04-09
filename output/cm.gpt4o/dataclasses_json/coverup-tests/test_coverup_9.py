# file dataclasses_json/core.py:211-231
# lines [211, 212, 216, 217, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 230, 231]
# branches ['212->216', '212->221', '216->217', '216->219', '221->222', '221->225', '225->226', '225->230']

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
    (datetime, datetime(2023, 1, 1, 12, 0, 0), datetime(2023, 1, 1, 12, 0, 0)),
    (datetime, 1672531200, datetime.fromtimestamp(1672531200, tz=timezone.utc)),
    (Decimal, Decimal('10.5'), Decimal('10.5')),
    (Decimal, '10.5', Decimal('10.5')),
    (UUID, UUID('12345678123456781234567812345678'), UUID('12345678123456781234567812345678')),
    (UUID, '12345678123456781234567812345678', UUID('12345678123456781234567812345678')),
    (str, 'test', 'test')
])
def test_support_extended_types(field_type, field_value, expected, mocker):
    mocker.patch('dataclasses_json.core._issubclass_safe', side_effect=_issubclass_safe)
    result = _support_extended_types(field_type, field_value)
    assert result == expected
