# file typesystem/fields.py:682-684
# lines [682, 683, 684]
# branches []

import pytest
from typesystem.fields import Date
from typesystem import ValidationError
from datetime import datetime

def test_date_field():
    date_field = Date(allow_null=True)

    # Test with a valid date string
    valid_date = "2023-03-25"
    expected_date = datetime.strptime(valid_date, '%Y-%m-%d').date()
    assert date_field.validate(valid_date) == expected_date

    # Test with an invalid date string
    invalid_date = "not-a-date"
    with pytest.raises(ValidationError):
        date_field.validate(invalid_date)

    # Test with None (assuming the field is allowed to be null)
    assert date_field.validate(None) is None

    # Cleanup is not necessary as no external state is modified
