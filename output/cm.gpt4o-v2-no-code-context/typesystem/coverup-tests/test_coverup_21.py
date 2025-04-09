# file: typesystem/formats.py:44-70
# asked: {"lines": [44, 45, 46, 47, 50, 51, 53, 54, 55, 56, 58, 59, 60, 61, 62, 64, 65, 66, 68, 70], "branches": [[55, 56], [55, 58], [65, 66], [65, 68]]}
# gained: {"lines": [44, 45, 46, 47, 50, 51, 53, 54, 55, 56, 58, 59, 60, 61, 62, 64, 65, 66, 68, 70], "branches": [[55, 56], [55, 58], [65, 66], [65, 68]]}

import pytest
import datetime
from typesystem.formats import DateFormat
from typesystem.base import ValidationError

def test_is_native_type_with_date():
    date_format = DateFormat()
    assert date_format.is_native_type(datetime.date.today()) is True

def test_is_native_type_with_non_date():
    date_format = DateFormat()
    assert date_format.is_native_type("2023-10-01") is False

def test_validate_with_valid_date():
    date_format = DateFormat()
    valid_date = "2023-10-01"
    result = date_format.validate(valid_date)
    assert result == datetime.date(2023, 10, 1)

def test_validate_with_invalid_format():
    date_format = DateFormat()
    invalid_date = "2023/10/01"
    with pytest.raises(ValidationError) as excinfo:
        date_format.validate(invalid_date)
    assert str(excinfo.value) == "Must be a valid date format."

def test_validate_with_nonexistent_date():
    date_format = DateFormat()
    nonexistent_date = "2023-02-30"
    with pytest.raises(ValidationError) as excinfo:
        date_format.validate(nonexistent_date)
    assert str(excinfo.value) == "Must be a real date."

def test_serialize_with_none():
    date_format = DateFormat()
    assert date_format.serialize(None) is None

def test_serialize_with_date():
    date_format = DateFormat()
    date_obj = datetime.date(2023, 10, 1)
    assert date_format.serialize(date_obj) == "2023-10-01"

def test_serialize_with_non_date():
    date_format = DateFormat()
    with pytest.raises(AssertionError):
        date_format.serialize("2023-10-01")
