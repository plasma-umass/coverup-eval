# file: typesystem/formats.py:106-154
# asked: {"lines": [132], "branches": [[131, 132]]}
# gained: {"lines": [132], "branches": [[131, 132]]}

import pytest
from typesystem.formats import DateTimeFormat
import datetime
from typesystem.base import ValidationError

def test_validate_negative_timezone():
    format = DateTimeFormat()
    value = "2023-10-05T14:48:00-05:30"
    result = format.validate(value)
    assert result == datetime.datetime(2023, 10, 5, 14, 48, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=-5, minutes=-30)))

def test_validate_positive_timezone():
    format = DateTimeFormat()
    value = "2023-10-05T14:48:00+05:30"
    result = format.validate(value)
    assert result == datetime.datetime(2023, 10, 5, 14, 48, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)))

def test_validate_utc_timezone():
    format = DateTimeFormat()
    value = "2023-10-05T14:48:00Z"
    result = format.validate(value)
    assert result == datetime.datetime(2023, 10, 5, 14, 48, 0, tzinfo=datetime.timezone.utc)

def test_validate_no_timezone():
    format = DateTimeFormat()
    value = "2023-10-05T14:48:00"
    result = format.validate(value)
    assert result == datetime.datetime(2023, 10, 5, 14, 48, 0)

def test_validate_invalid_format():
    format = DateTimeFormat()
    value = "invalid-datetime"
    with pytest.raises(ValidationError):
        format.validate(value)

def test_validate_invalid_datetime():
    format = DateTimeFormat()
    value = "2023-13-05T14:48:00"  # Invalid month
    with pytest.raises(ValidationError):
        format.validate(value)
