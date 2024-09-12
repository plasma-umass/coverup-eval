# file: typesystem/formats.py:73-103
# asked: {"lines": [73, 74, 75, 76, 79, 80, 82, 83, 84, 85, 87, 88, 89, 91, 92, 93, 94, 95, 97, 98, 99, 101, 103], "branches": [[84, 85], [84, 87], [88, 89], [88, 91], [98, 99], [98, 101]]}
# gained: {"lines": [73, 74, 75, 76, 79, 80, 82, 83, 84, 85, 87, 88, 89, 91, 92, 93, 94, 95, 97, 98, 99, 101, 103], "branches": [[84, 85], [84, 87], [88, 89], [88, 91], [98, 99], [98, 101]]}

import pytest
import datetime
from typesystem.formats import TimeFormat
from typesystem import ValidationError

@pytest.fixture
def time_format():
    return TimeFormat()

def test_is_native_type_with_time(time_format):
    assert time_format.is_native_type(datetime.time(12, 0)) is True

def test_is_native_type_with_non_time(time_format):
    assert time_format.is_native_type("12:00") is False

def test_validate_with_valid_time(time_format):
    valid_time = "12:34:56.789"
    result = time_format.validate(valid_time)
    assert result == datetime.time(12, 34, 56, 789000)

def test_validate_with_invalid_format(time_format):
    invalid_time = "invalid"
    with pytest.raises(ValidationError, match="Must be a valid time format."):
        time_format.validate(invalid_time)

def test_validate_with_invalid_time(time_format):
    invalid_time = "25:00:00"
    with pytest.raises(ValidationError, match="Must be a real time."):
        time_format.validate(invalid_time)

def test_serialize_with_none(time_format):
    assert time_format.serialize(None) is None

def test_serialize_with_time(time_format):
    time_obj = datetime.time(12, 34, 56)
    assert time_format.serialize(time_obj) == "12:34:56"
