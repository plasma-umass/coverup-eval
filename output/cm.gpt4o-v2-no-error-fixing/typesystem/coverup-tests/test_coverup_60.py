# file: typesystem/formats.py:106-154
# asked: {"lines": [113, 116, 117, 118, 120, 121, 122, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 135, 137, 138, 139, 140, 141, 144, 145, 147, 149, 151, 152, 154], "branches": [[117, 118], [117, 120], [121, 122], [121, 124], [125, 126], [125, 127], [127, 128], [127, 135], [131, 132], [131, 133], [144, 145], [144, 147], [151, 152], [151, 154]]}
# gained: {"lines": [113, 116, 117, 118, 120, 121, 124, 125, 126, 137, 138, 139, 140, 141, 144, 145, 147, 149, 151, 152, 154], "branches": [[117, 118], [117, 120], [121, 124], [125, 126], [144, 145], [144, 147], [151, 152], [151, 154]]}

import pytest
import datetime
from typesystem.formats import DateTimeFormat

@pytest.fixture
def datetime_format():
    return DateTimeFormat()

def test_is_native_type_with_datetime(datetime_format):
    assert datetime_format.is_native_type(datetime.datetime.now()) is True

def test_is_native_type_with_non_datetime(datetime_format):
    assert datetime_format.is_native_type("2023-10-01T00:00:00") is False

def test_validate_with_valid_datetime(datetime_format):
    valid_datetime_str = "2023-10-01T00:00:00Z"
    result = datetime_format.validate(valid_datetime_str)
    assert result == datetime.datetime(2023, 10, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)

def test_validate_with_invalid_format(datetime_format):
    invalid_datetime_str = "invalid-datetime"
    with pytest.raises(Exception) as excinfo:
        datetime_format.validate(invalid_datetime_str)
    assert "Must be a valid datetime format." in str(excinfo.value)

def test_validate_with_invalid_datetime(datetime_format):
    invalid_datetime_str = "2023-13-01T00:00:00Z"  # Invalid month
    with pytest.raises(Exception) as excinfo:
        datetime_format.validate(invalid_datetime_str)
    assert "Must be a real datetime." in str(excinfo.value)

def test_serialize_with_none(datetime_format):
    assert datetime_format.serialize(None) is None

def test_serialize_with_valid_datetime(datetime_format):
    dt = datetime.datetime(2023, 10, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
    assert datetime_format.serialize(dt) == "2023-10-01T00:00:00Z"

def test_serialize_with_non_utc_timezone(datetime_format):
    tzinfo = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    dt = datetime.datetime(2023, 10, 1, 0, 0, 0, tzinfo=tzinfo)
    assert datetime_format.serialize(dt) == "2023-10-01T00:00:00+05:30"
