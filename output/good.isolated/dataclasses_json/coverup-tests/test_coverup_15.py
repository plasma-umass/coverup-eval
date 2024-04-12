# file dataclasses_json/core.py:211-231
# lines [211, 212, 216, 217, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 230, 231]
# branches ['212->216', '212->221', '216->217', '216->219', '221->222', '221->225', '225->226', '225->230']

import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
from dataclasses_json.core import _issubclass_safe

# Mock function to replace _issubclass_safe for testing purposes
def mock_issubclass_safe(cls, classinfo):
    return issubclass(cls, classinfo)

@pytest.fixture
def mock_issubclass_safe_fixture(mocker):
    mocker.patch('dataclasses_json.core._issubclass_safe', side_effect=mock_issubclass_safe)

def test_support_extended_types_datetime(mock_issubclass_safe_fixture):
    from dataclasses_json.core import _support_extended_types
    dt = datetime.now()
    timestamp = dt.timestamp()
    result = _support_extended_types(datetime, timestamp)
    assert isinstance(result, datetime)
    assert result == datetime.fromtimestamp(timestamp, tz=datetime.now(timezone.utc).astimezone().tzinfo)

def test_support_extended_types_decimal(mock_issubclass_safe_fixture):
    from dataclasses_json.core import _support_extended_types
    dec_str = "10.5"
    dec = Decimal(dec_str)
    result = _support_extended_types(Decimal, dec_str)
    assert isinstance(result, Decimal)
    assert result == dec

def test_support_extended_types_uuid(mock_issubclass_safe_fixture):
    from dataclasses_json.core import _support_extended_types
    uuid_str = "12345678-1234-5678-1234-567812345678"
    uuid_obj = UUID(uuid_str)
    result = _support_extended_types(UUID, uuid_str)
    assert isinstance(result, UUID)
    assert result == uuid_obj

def test_support_extended_types_no_extended_type(mock_issubclass_safe_fixture):
    from dataclasses_json.core import _support_extended_types
    value = "test"
    result = _support_extended_types(str, value)
    assert result == value
