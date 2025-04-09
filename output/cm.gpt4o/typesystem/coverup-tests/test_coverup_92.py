# file typesystem/formats.py:73-103
# lines [80, 83, 84, 85, 87, 88, 89, 91, 92, 93, 94, 95, 98, 99, 101, 103]
# branches ['84->85', '84->87', '88->89', '88->91', '98->99', '98->101']

import pytest
import datetime
from typesystem.formats import TimeFormat
from typesystem import ValidationError

def test_time_format_is_native_type():
    time_format = TimeFormat()
    assert time_format.is_native_type(datetime.time(12, 0)) is True
    assert time_format.is_native_type("12:00") is False

def test_time_format_validate():
    time_format = TimeFormat()
    
    # Valid time string
    valid_time = "12:34:56.789"
    result = time_format.validate(valid_time)
    assert result == datetime.time(12, 34, 56, 789000)
    
    # Invalid time format
    with pytest.raises(ValidationError) as excinfo:
        time_format.validate("invalid time")
    assert str(excinfo.value) == "Must be a valid time format."
    
    # Invalid time value
    with pytest.raises(ValidationError) as excinfo:
        time_format.validate("25:00:00")
    assert str(excinfo.value) == "Must be a real time."

def test_time_format_serialize():
    time_format = TimeFormat()
    
    # None input
    assert time_format.serialize(None) is None
    
    # Valid datetime.time object
    time_obj = datetime.time(12, 34, 56)
    assert time_format.serialize(time_obj) == "12:34:56"
    
    # Invalid input type
    with pytest.raises(AssertionError):
        time_format.serialize("12:34:56")
