# file typesystem/formats.py:73-103
# lines [73, 74, 75, 76, 79, 80, 82, 83, 84, 85, 87, 88, 89, 91, 92, 93, 94, 95, 97, 98, 99, 101, 103]
# branches ['84->85', '84->87', '88->89', '88->91', '98->99', '98->101']

import pytest
import datetime
import typing
from typesystem.formats import BaseFormat
import re
from typesystem import ValidationError

TIME_REGEX = re.compile(
    r"^(?P<hour>\d{2}):(?P<minute>\d{2})(?::(?P<second>\d{2})(?:\.(?P<microsecond>\d{1,6}))?)?$"
)

class TimeFormat(BaseFormat):
    errors = {
        "format": "Must be a valid time format.",
        "invalid": "Must be a real time.",
    }

    def is_native_type(self, value: typing.Any) -> bool:
        return isinstance(value, datetime.time)

    def validate(self, value: typing.Any) -> datetime.time:
        match = TIME_REGEX.match(value)
        if not match:
            raise self.validation_error("format")

        groups = match.groupdict()
        if groups["microsecond"]:
            groups["microsecond"] = groups["microsecond"].ljust(6, "0")

        kwargs = {k: int(v) for k, v in groups.items() if v is not None}
        try:
            return datetime.time(tzinfo=None, **kwargs)
        except ValueError:
            raise self.validation_error("invalid")

    def serialize(self, obj: typing.Any) -> typing.Union[str, None]:
        if obj is None:
            return None

        assert isinstance(obj, datetime.time)

        return obj.isoformat()

@pytest.fixture
def time_format():
    return TimeFormat()

def test_is_native_type(time_format):
    assert time_format.is_native_type(datetime.time(12, 0))
    assert not time_format.is_native_type("12:00")

def test_validate_valid_time(time_format):
    assert time_format.validate("12:34:56.789") == datetime.time(12, 34, 56, 789000)
    assert time_format.validate("12:34:56") == datetime.time(12, 34, 56)
    assert time_format.validate("12:34") == datetime.time(12, 34)

def test_validate_invalid_format(time_format):
    with pytest.raises(ValidationError, match="Must be a valid time format."):
        time_format.validate("invalid")

def test_validate_invalid_time(time_format):
    with pytest.raises(ValidationError, match="Must be a real time."):
        time_format.validate("25:00")

def test_serialize(time_format):
    assert time_format.serialize(datetime.time(12, 34, 56, 789000)) == "12:34:56.789000"
    assert time_format.serialize(datetime.time(12, 34, 56)) == "12:34:56"
    assert time_format.serialize(datetime.time(12, 34)) == "12:34:00"
    assert time_format.serialize(None) is None
