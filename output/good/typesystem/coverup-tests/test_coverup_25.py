# file typesystem/formats.py:73-103
# lines [73, 74, 75, 76, 79, 80, 82, 83, 84, 85, 87, 88, 89, 91, 92, 93, 94, 95, 97, 98, 99, 101, 103]
# branches ['84->85', '84->87', '88->89', '88->91', '98->99', '98->101']

import datetime
import re
import pytest
from typesystem import ValidationError
from typesystem.formats import TimeFormat

TIME_REGEX = re.compile(
    r"^(?P<hour>\d{2}):(?P<minute>\d{2})"
    r"(?::(?P<second>\d{2})(?:\.(?P<microsecond>\d{1,6}))?)?$"
)

@pytest.fixture
def time_format():
    return TimeFormat()

def test_time_format_valid(time_format):
    valid_time = "14:30:59.123456"
    result = time_format.validate(valid_time)
    assert result == datetime.time(14, 30, 59, 123456)

def test_time_format_invalid_format(time_format):
    invalid_time = "not-a-time"
    with pytest.raises(ValidationError) as exc_info:
        time_format.validate(invalid_time)
    assert str(exc_info.value) == time_format.errors["format"]

def test_time_format_invalid_real_time(time_format):
    invalid_time = "25:61:61"
    with pytest.raises(ValidationError) as exc_info:
        time_format.validate(invalid_time)
    assert str(exc_info.value) == time_format.errors["invalid"]

def test_time_format_serialize_none(time_format):
    assert time_format.serialize(None) is None

def test_time_format_serialize_valid_time(time_format):
    valid_time = datetime.time(14, 30, 59, 123456)
    result = time_format.serialize(valid_time)
    assert result == "14:30:59.123456"

def test_time_format_serialize_invalid_type(time_format):
    invalid_time = "14:30:59.123456"
    with pytest.raises(AssertionError):
        time_format.serialize(invalid_time)
