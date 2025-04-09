# file typesystem/fields.py:692-694
# lines [692, 693, 694]
# branches []

import pytest
from typesystem.fields import DateTime
from typesystem import ValidationError
from datetime import datetime, timezone

def test_datetime_field():
    # Test valid datetime string
    datetime_field = DateTime()
    valid_datetime = "2023-03-20T12:00:00Z"
    expected_datetime = datetime(2023, 3, 20, 12, 0, tzinfo=timezone.utc)
    assert datetime_field.validate(valid_datetime) == expected_datetime

    # Test invalid datetime string
    with pytest.raises(ValidationError):
        invalid_datetime = "not-a-datetime"
        datetime_field.validate(invalid_datetime)
