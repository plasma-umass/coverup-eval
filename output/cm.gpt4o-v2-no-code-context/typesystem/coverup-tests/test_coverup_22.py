# file: typesystem/formats.py:106-154
# asked: {"lines": [106, 107, 108, 109, 112, 113, 115, 116, 117, 118, 120, 121, 122, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 135, 137, 138, 139, 140, 141, 143, 144, 145, 147, 149, 151, 152, 154], "branches": [[117, 118], [117, 120], [121, 122], [121, 124], [125, 126], [125, 127], [127, 128], [127, 135], [131, 132], [131, 133], [144, 145], [144, 147], [151, 152], [151, 154]]}
# gained: {"lines": [106, 107, 108, 109, 112, 113, 115, 116, 117, 118, 120, 121, 122, 124, 125, 126, 127, 128, 129, 130, 131, 133, 137, 138, 139, 140, 141, 143, 144, 145, 147, 149, 151, 152, 154], "branches": [[117, 118], [117, 120], [121, 122], [121, 124], [125, 126], [125, 127], [127, 128], [131, 133], [144, 145], [144, 147], [151, 152], [151, 154]]}

import pytest
import datetime
from typesystem.formats import DateTimeFormat
from typesystem import ValidationError

def test_is_native_type():
    format = DateTimeFormat()
    assert format.is_native_type(datetime.datetime.now()) is True
    assert format.is_native_type("2023-10-01T12:00:00Z") is False

def test_validate_valid_datetime():
    format = DateTimeFormat()
    dt_str = "2023-10-01T12:00:00Z"
    dt = format.validate(dt_str)
    assert dt == datetime.datetime(2023, 10, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)

def test_validate_invalid_format():
    format = DateTimeFormat()
    with pytest.raises(ValidationError, match="Must be a valid datetime format."):
        format.validate("invalid-datetime")

def test_validate_invalid_datetime():
    format = DateTimeFormat()
    with pytest.raises(ValidationError, match="Must be a real datetime."):
        format.validate("2023-02-30T12:00:00Z")

def test_validate_with_microseconds():
    format = DateTimeFormat()
    dt_str = "2023-10-01T12:00:00.123Z"
    dt = format.validate(dt_str)
    assert dt == datetime.datetime(2023, 10, 1, 12, 0, 0, 123000, tzinfo=datetime.timezone.utc)

def test_validate_with_timezone_offset():
    format = DateTimeFormat()
    dt_str = "2023-10-01T12:00:00+02:30"
    dt = format.validate(dt_str)
    assert dt == datetime.datetime(2023, 10, 1, 12, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=2, minutes=30)))

def test_serialize_none():
    format = DateTimeFormat()
    assert format.serialize(None) is None

def test_serialize_datetime():
    format = DateTimeFormat()
    dt = datetime.datetime(2023, 10, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
    assert format.serialize(dt) == "2023-10-01T12:00:00Z"

def test_serialize_datetime_with_offset():
    format = DateTimeFormat()
    dt = datetime.datetime(2023, 10, 1, 12, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=2, minutes=30)))
    assert format.serialize(dt) == "2023-10-01T12:00:00+02:30"
