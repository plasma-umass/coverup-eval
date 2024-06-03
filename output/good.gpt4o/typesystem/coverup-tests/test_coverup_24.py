# file typesystem/formats.py:106-154
# lines [106, 107, 108, 109, 112, 113, 115, 116, 117, 118, 120, 121, 122, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 135, 137, 138, 139, 140, 141, 143, 144, 145, 147, 149, 151, 152, 154]
# branches ['117->118', '117->120', '121->122', '121->124', '125->126', '125->127', '127->128', '127->135', '131->132', '131->133', '144->145', '144->147', '151->152', '151->154']

import pytest
import datetime
from typesystem.formats import DateTimeFormat
from typesystem import ValidationError

def test_datetime_format_is_native_type():
    dt_format = DateTimeFormat()
    assert dt_format.is_native_type(datetime.datetime.now()) is True
    assert dt_format.is_native_type("2023-10-01T12:00:00Z") is False

def test_datetime_format_validate():
    dt_format = DateTimeFormat()
    
    # Valid datetime with microseconds and timezone
    valid_datetime = "2023-10-01T12:00:00.123456+02:00"
    result = dt_format.validate(valid_datetime)
    assert result == datetime.datetime(2023, 10, 1, 12, 0, 0, 123456, tzinfo=datetime.timezone(datetime.timedelta(hours=2)))
    
    # Valid datetime with 'Z' timezone
    valid_datetime_z = "2023-10-01T12:00:00Z"
    result = dt_format.validate(valid_datetime_z)
    assert result == datetime.datetime(2023, 10, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
    
    # Invalid datetime format
    with pytest.raises(ValidationError, match="Must be a valid datetime format."):
        dt_format.validate("invalid-datetime")
    
    # Invalid datetime value
    with pytest.raises(ValidationError, match="Must be a real datetime."):
        dt_format.validate("2023-13-01T12:00:00Z")  # Invalid month

def test_datetime_format_serialize():
    dt_format = DateTimeFormat()
    
    # Serialize datetime with timezone
    dt = datetime.datetime(2023, 10, 1, 12, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=2)))
    assert dt_format.serialize(dt) == "2023-10-01T12:00:00+02:00"
    
    # Serialize datetime with 'Z' timezone
    dt_z = datetime.datetime(2023, 10, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
    assert dt_format.serialize(dt_z) == "2023-10-01T12:00:00Z"
    
    # Serialize None
    assert dt_format.serialize(None) is None

@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
