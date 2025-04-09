# file typesystem/formats.py:44-70
# lines [44, 45, 46, 47, 50, 51, 53, 54, 55, 56, 58, 59, 60, 61, 62, 64, 65, 66, 68, 70]
# branches ['55->56', '55->58', '65->66', '65->68']

import datetime
import pytest
from typesystem import ValidationError
from typesystem.formats import DateFormat

DATE_REGEX = r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})$"

def test_date_format_validation():
    date_format = DateFormat()

    # Test valid date
    valid_date = "2023-03-25"
    result = date_format.validate(valid_date)
    assert result == datetime.date(2023, 3, 25)

    # Test invalid date format
    invalid_date_format = "25-03-2023"
    with pytest.raises(ValidationError) as exc_info:
        date_format.validate(invalid_date_format)
    assert str(exc_info.value) == "Must be a valid date format."

    # Test invalid real date
    invalid_real_date = "2023-02-30"
    with pytest.raises(ValidationError) as exc_info:
        date_format.validate(invalid_real_date)
    assert str(exc_info.value) == "Must be a real date."

    # Test serialization of None
    assert date_format.serialize(None) is None

    # Test serialization of a valid date object
    date_obj = datetime.date(2023, 3, 25)
    assert date_format.serialize(date_obj) == "2023-03-25"

    # Test is_native_type with a date object
    assert date_format.is_native_type(date_obj) is True

    # Test is_native_type with a non-date object
    assert date_format.is_native_type("2023-03-25") is False
