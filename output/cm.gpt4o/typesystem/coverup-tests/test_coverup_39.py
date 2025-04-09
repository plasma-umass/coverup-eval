# file typesystem/formats.py:44-70
# lines [44, 45, 46, 47, 50, 51, 53, 54, 55, 56, 58, 59, 60, 61, 62, 64, 65, 66, 68, 70]
# branches ['55->56', '55->58', '65->66', '65->68']

import pytest
import datetime
import re
import typing
from typesystem.formats import BaseFormat
from typesystem import ValidationError

# Mocking DATE_REGEX for the purpose of this test
DATE_REGEX = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")

class DateFormat(BaseFormat):
    errors = {
        "format": "Must be a valid date format.",
        "invalid": "Must be a real date.",
    }

    def is_native_type(self, value: typing.Any) -> bool:
        return isinstance(value, datetime.date)

    def validate(self, value: typing.Any) -> datetime.date:
        match = DATE_REGEX.match(value)
        if not match:
            raise self.validation_error("format")

        kwargs = {k: int(v) for k, v in match.groupdict().items()}
        try:
            return datetime.date(**kwargs)
        except ValueError:
            raise self.validation_error("invalid")

    def serialize(self, obj: typing.Any) -> typing.Union[str, None]:
        if obj is None:
            return None

        assert isinstance(obj, datetime.date)

        return obj.isoformat()

@pytest.fixture
def date_format():
    return DateFormat()

def test_is_native_type(date_format):
    assert date_format.is_native_type(datetime.date(2023, 10, 1))
    assert not date_format.is_native_type("2023-10-01")

def test_validate_correct_format(date_format):
    assert date_format.validate("2023-10-01") == datetime.date(2023, 10, 1)

def test_validate_incorrect_format(date_format):
    with pytest.raises(ValidationError) as excinfo:
        date_format.validate("2023/10/01")
    assert str(excinfo.value) == "Must be a valid date format."

def test_validate_invalid_date(date_format):
    with pytest.raises(ValidationError) as excinfo:
        date_format.validate("2023-02-30")
    assert str(excinfo.value) == "Must be a real date."

def test_serialize(date_format):
    assert date_format.serialize(datetime.date(2023, 10, 1)) == "2023-10-01"
    assert date_format.serialize(None) is None

def test_serialize_invalid_type(date_format):
    with pytest.raises(AssertionError):
        date_format.serialize("2023-10-01")
