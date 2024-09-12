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

def test_validate():
    date_format = DateFormat()
    
    # Valid date
    valid_date = "2023-10-05"
    result = date_format.validate(valid_date)
    assert result == datetime.date(2023, 10, 5)
    
    # Invalid format
    with pytest.raises(ValidationError) as excinfo:
        date_format.validate("2023/10/05")
    assert str(excinfo.value) == "Must be a valid date format."
    
    # Invalid date
    with pytest.raises(ValidationError) as excinfo:
        date_format.validate("2023-02-30")
    assert str(excinfo.value) == "Must be a real date."

def test_serialize():
    date_format = DateFormat()
    
    # None input
    assert date_format.serialize(None) is None
    
    # Valid date object
    date_obj = datetime.date(2023, 10, 5)
    assert date_format.serialize(date_obj) == "2023-10-05"
    
    # Invalid type
    with pytest.raises(AssertionError):
        date_format.serialize("2023-10-05")
