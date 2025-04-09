# file: typesystem/formats.py:44-70
# asked: {"lines": [44, 45, 46, 47, 50, 51, 53, 54, 55, 56, 58, 59, 60, 61, 62, 64, 65, 66, 68, 70], "branches": [[55, 56], [55, 58], [65, 66], [65, 68]]}
# gained: {"lines": [44, 45, 46, 47, 50, 51, 53, 54, 55, 56, 58, 59, 60, 61, 62, 64, 65, 66, 68, 70], "branches": [[55, 56], [55, 58], [65, 66], [65, 68]]}

import pytest
import datetime
from typesystem.formats import DateFormat
from typesystem.base import ValidationError

def test_is_native_type():
    date_format = DateFormat()
    assert date_format.is_native_type(datetime.date.today()) is True
    assert date_format.is_native_type("2023-10-05") is False

def test_validate_valid_date():
    date_format = DateFormat()
    valid_date_str = "2023-10-05"
    expected_date = datetime.date(2023, 10, 5)
    assert date_format.validate(valid_date_str) == expected_date

def test_validate_invalid_format():
    date_format = DateFormat()
    invalid_date_str = "2023/10/05"
    with pytest.raises(ValidationError) as exc_info:
        date_format.validate(invalid_date_str)
    assert str(exc_info.value) == "Must be a valid date format."

def test_validate_invalid_date():
    date_format = DateFormat()
    invalid_date_str = "2023-02-30"
    with pytest.raises(ValidationError) as exc_info:
        date_format.validate(invalid_date_str)
    assert str(exc_info.value) == "Must be a real date."

def test_serialize_none():
    date_format = DateFormat()
    assert date_format.serialize(None) is None

def test_serialize_valid_date():
    date_format = DateFormat()
    date_obj = datetime.date(2023, 10, 5)
    assert date_format.serialize(date_obj) == "2023-10-05"

def test_serialize_invalid_type():
    date_format = DateFormat()
    with pytest.raises(AssertionError):
        date_format.serialize("2023-10-05")
