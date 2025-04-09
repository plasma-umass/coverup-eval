# file: typesystem/formats.py:73-103
# asked: {"lines": [80, 83, 84, 85, 87, 88, 89, 91, 92, 93, 94, 95, 98, 99, 101, 103], "branches": [[84, 85], [84, 87], [88, 89], [88, 91], [98, 99], [98, 101]]}
# gained: {"lines": [80, 83, 84, 85, 87, 88, 89, 91, 92, 93, 94, 95, 98, 99, 101, 103], "branches": [[84, 85], [84, 87], [88, 89], [88, 91], [98, 99], [98, 101]]}

import pytest
import datetime
from typesystem.formats import TimeFormat

class MockBaseFormat:
    def validation_error(self, error_type):
        return ValueError(TimeFormat.errors[error_type])

@pytest.fixture
def time_format():
    return TimeFormat()

def test_is_native_type(time_format):
    assert time_format.is_native_type(datetime.time(12, 0)) is True
    assert time_format.is_native_type("12:00") is False

def test_validate_valid_time(monkeypatch, time_format):
    import re
    TIME_REGEX = re.compile(
        r"^(?P<hour>\d{2}):(?P<minute>\d{2})(?::(?P<second>\d{2})(?:\.(?P<microsecond>\d{1,6}))?)?$"
    )
    monkeypatch.setattr("typesystem.formats.TIME_REGEX", TIME_REGEX)
    monkeypatch.setattr(TimeFormat, "validation_error", MockBaseFormat().validation_error)
    
    assert time_format.validate("12:34:56.789") == datetime.time(12, 34, 56, 789000)
    assert time_format.validate("12:34:56") == datetime.time(12, 34, 56)
    assert time_format.validate("12:34") == datetime.time(12, 34)

def test_validate_invalid_format(monkeypatch, time_format):
    import re
    TIME_REGEX = re.compile(
        r"^(?P<hour>\d{2}):(?P<minute>\d{2})(?::(?P<second>\d{2})(?:\.(?P<microsecond>\d{1,6}))?)?$"
    )
    monkeypatch.setattr("typesystem.formats.TIME_REGEX", TIME_REGEX)
    monkeypatch.setattr(TimeFormat, "validation_error", MockBaseFormat().validation_error)
    
    with pytest.raises(ValueError, match="Must be a valid time format."):
        time_format.validate("invalid")

def test_validate_invalid_time(monkeypatch, time_format):
    import re
    TIME_REGEX = re.compile(
        r"^(?P<hour>\d{2}):(?P<minute>\d{2})(?::(?P<second>\d{2})(?:\.(?P<microsecond>\d{1,6}))?)?$"
    )
    monkeypatch.setattr("typesystem.formats.TIME_REGEX", TIME_REGEX)
    monkeypatch.setattr(TimeFormat, "validation_error", MockBaseFormat().validation_error)
    
    with pytest.raises(ValueError, match="Must be a real time."):
        time_format.validate("25:00")

def test_serialize(time_format):
    assert time_format.serialize(None) is None
    assert time_format.serialize(datetime.time(12, 34, 56)) == "12:34:56"
    assert time_format.serialize(datetime.time(12, 34, 56, 789000)) == "12:34:56.789000"
