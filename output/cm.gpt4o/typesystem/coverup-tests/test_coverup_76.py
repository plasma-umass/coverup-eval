# file typesystem/formats.py:106-154
# lines [132, 135]
# branches ['127->135', '131->132']

import pytest
import datetime
from typesystem.formats import DateTimeFormat

def test_datetime_format_with_negative_timezone():
    format = DateTimeFormat()
    value = "2023-10-05T14:48:00-05:00"
    result = format.validate(value)
    assert result == datetime.datetime(2023, 10, 5, 14, 48, tzinfo=datetime.timezone(datetime.timedelta(hours=-5)))

def test_datetime_format_with_no_timezone():
    format = DateTimeFormat()
    value = "2023-10-05T14:48:00"
    result = format.validate(value)
    assert result == datetime.datetime(2023, 10, 5, 14, 48, tzinfo=None)
